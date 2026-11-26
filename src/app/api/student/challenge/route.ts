import { NextResponse } from "next/server";
import { getDatabase, saveDatabase } from "@/lib/storage";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { submissionId, decision, challenges } = body;
    // challenges is an array: [ { questionId: string, reason: string } ]

    const db = getDatabase();
    const sub = db.submissions.find(s => s.id === submissionId);

    if (!sub) {
      return NextResponse.json({ error: "Submission not found" }, { status: 404 });
    }

    if (decision === "ACCEPT") {
      sub.status = "ACCEPTED";
      sub.acceptedAt = new Date().toISOString();
      saveDatabase(db);
      return NextResponse.json({
        success: true,
        submission: sub,
        message: "You have accepted the final evaluated marks. Your score is archived in your academic record."
      });
    }

    if (decision === "CHALLENGE") {
      if (!challenges || challenges.length === 0) {
        return NextResponse.json({ error: "Please select at least one question to challenge." }, { status: 400 });
      }

      sub.status = "CHALLENGED";
      sub.challengedAt = new Date().toISOString();

      for (const ch of challenges) {
        const q = sub.questions.find(item => item.questionId === ch.questionId);
        if (q) {
          q.isChallenged = true;
          q.studentChallengeReason = ch.reason || "Student requested re-evaluation of step marking.";
        }
      }

      saveDatabase(db);
      return NextResponse.json({
        success: true,
        submission: sub,
        message: "Your challenge has been submitted to the Subject Teacher for re-evaluation."
      });
    }

    return NextResponse.json({ error: "Invalid decision" }, { status: 400 });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Failed to process challenge" }, { status: 500 });
  }
}
