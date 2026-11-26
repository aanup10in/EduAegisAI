import { NextResponse } from "next/server";
import { getDatabase, saveDatabase } from "@/lib/storage";

export async function GET() {
  const db = getDatabase();
  return NextResponse.json({
    submissions: db.submissions,
    teacherInstructions: db.teacherInstructions
  });
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { action, submissionId, questionId, newMarks, teacherFeedback, instructionData, resolutionNotes } = body;
    const db = getDatabase();

    if (action === "SAVE_INSTRUCTIONS") {
      const { topicId, specificInstructions, strictSIUnits, partialCreditForSteps, lenientSpelling } = instructionData;
      db.teacherInstructions[topicId] = {
        id: "instr_" + Date.now(),
        topicId,
        specificInstructions,
        strictSIUnits: Boolean(strictSIUnits),
        partialCreditForSteps: Boolean(partialCreditForSteps),
        lenientSpelling: Boolean(lenientSpelling),
        weights: { facts: 0.3, concepts: 0.4, terminology: 0.2, derivation: 0.1 },
        updatedAt: new Date().toISOString()
      };
      saveDatabase(db);
      return NextResponse.json({ success: true, instruction: db.teacherInstructions[topicId] });
    }

    const sub = db.submissions.find(s => s.id === submissionId);
    if (!sub) {
      return NextResponse.json({ error: "Submission not found" }, { status: 404 });
    }

    if (action === "RELEASE_MARKS") {
      sub.status = "RELEASED";
      sub.releasedAt = new Date().toISOString();
      if (teacherFeedback) {
        sub.teacherOverallFeedback = teacherFeedback;
      }
      saveDatabase(db);
      return NextResponse.json({ success: true, submission: sub, message: "Marks released to student successfully." });
    }

    if (action === "UPDATE_MARKS") {
      const q = sub.questions.find(item => item.questionId === questionId);
      if (q) {
        q.teacherOverrideMarks = Number(newMarks);
        q.awardedMarks = Number(newMarks);
      }
      // Re-sum total
      sub.totalAwardedMarks = sub.questions.reduce((sum, item) => sum + (item.teacherOverrideMarks ?? item.awardedMarks), 0);
      sub.totalAwardedMarks = Math.round(sub.totalAwardedMarks * 10) / 10;
      saveDatabase(db);
      return NextResponse.json({ success: true, submission: sub });
    }

    if (action === "RESOLVE_CHALLENGE") {
      const q = sub.questions.find(item => item.questionId === questionId);
      if (q) {
        if (newMarks !== undefined) {
          q.teacherOverrideMarks = Number(newMarks);
          q.awardedMarks = Number(newMarks);
        }
        q.teacherChallengeResolution = resolutionNotes || "Reviewed by Senior Physics Faculty. Marks updated accordingly.";
        q.isChallenged = false;
      }
      // Re-sum total
      sub.totalAwardedMarks = sub.questions.reduce((sum, item) => sum + (item.teacherOverrideMarks ?? item.awardedMarks), 0);
      sub.totalAwardedMarks = Math.round(sub.totalAwardedMarks * 10) / 10;
      sub.status = "RELEASED"; // Re-released after resolution
      saveDatabase(db);
      return NextResponse.json({ success: true, submission: sub, message: "Challenge resolved and updated scores published." });
    }

    return NextResponse.json({ error: "Invalid action" }, { status: 400 });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Teacher operation failed" }, { status: 500 });
  }
}
