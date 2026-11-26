import { NextResponse } from "next/server";
import { getDatabase, saveDatabase, SubjectiveSubmission, QuestionGrading } from "@/lib/storage";
import { evaluateStudentAnswer } from "@/lib/evaluator";
import { CURRICULUM_DATA, generateDynamicTopicContent, Chapter } from "@/lib/curriculum";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const {
      studentId,
      studentName,
      board,
      className,
      subjectId,
      chapterId,
      customTopicTitle,
      answers, // record of questionId -> studentAnswer
      teacherInstructionsOverride
    } = body;

    const db = getDatabase();
    const classNum = parseInt(className?.replace(/[^0-9]/g, "") || "9", 10) || 9;
    const cur = CURRICULUM_DATA[classNum] || CURRICULUM_DATA[9];
    const subject = cur.subjects.find((s) => s.id === (subjectId || "physics")) || cur.subjects[0];

    let chapter: Chapter | undefined;

    // Check if custom topic title was provided
    if (customTopicTitle && customTopicTitle.trim()) {
      chapter = generateDynamicTopicContent(
        customTopicTitle,
        subject.name,
        classNum,
        board || "CBSE (All India)"
      );
    } else {
      chapter = subject.chapters.find((c) => c.id === chapterId) || subject.chapters[0];
    }

    if (!chapter) {
      chapter = generateDynamicTopicContent("Core Concepts", subject.name, classNum, board || "CBSE");
    }

    const paper = chapter.subjectivePaper;
    const teacherInst = teacherInstructionsOverride || db.teacherInstructions[chapter.id];

    const gradedQuestions: QuestionGrading[] = [];
    let totalMax = 0;
    let totalAwarded = 0;

    for (const q of paper) {
      totalMax += q.maxMarks;
      const studentAnsText = answers[q.id] || "";

      const graded = evaluateStudentAnswer({
        questionId: q.id,
        questionText: q.question,
        studentAnswer: studentAnsText,
        maxMarks: q.maxMarks,
        modelAnswer: q.modelAnswer,
        rubricPoints: q.rubricPoints,
        referenceChapter: `${chapter.title} (${chapter.ncertChapter})`,
        authenticReferences: chapter.concepts[0]?.authenticReferences || [
          {
            title: `NCERT Class ${classNum} Official Portal`,
            url: "https://ncert.nic.in",
            source: "NCERT"
          }
        ],
        teacherInstruction: teacherInst,
        board: board || "CBSE (All India)",
        subject: subject.name
      });

      gradedQuestions.push(graded);
      totalAwarded += graded.awardedMarks;
    }

    totalAwarded = Math.round(totalAwarded * 10) / 10;

    const submission: SubjectiveSubmission = {
      id: "sub_" + Date.now(),
      studentId: studentId || "std_default_aarav",
      studentName: studentName || "Aarav Sharma",
      board: board || "CBSE (All India)",
      className: `Class ${classNum}th`,
      subjectName: subject.name,
      chapterTitle: chapter.title,
      topicName: chapter.title,
      submittedAt: new Date().toISOString(),
      totalMaxMarks: totalMax,
      totalAwardedMarks: totalAwarded,
      status: "PENDING_TEACHER_RELEASE", // AI Governance: Human-in-the-Loop release required
      teacherInstructionsUsed: teacherInst?.specificInstructions || "Standard Multi-Subject NCERT Rubric",
      questions: gradedQuestions
    };

    db.submissions.unshift(submission);
    saveDatabase(db);

    return NextResponse.json({
      success: true,
      submission
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Evaluation failed" }, { status: 500 });
  }
}
