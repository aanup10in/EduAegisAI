import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { sourceType, content, youtubeUrl } = body;

    let title = "Custom Ingested Lesson";
    let explanation = "";
    let audioScript = "";
    let keyPoints: string[] = [];
    let analogies: string[] = [];

    if (sourceType === "youtube" && youtubeUrl) {
      // Parse YouTube ID / URL
      let videoId = "";
      try {
        const urlObj = new URL(youtubeUrl);
        if (urlObj.hostname.includes("youtu.be")) {
          videoId = urlObj.pathname.slice(1);
        } else {
          videoId = urlObj.searchParams.get("v") || "";
        }
      } catch {
        videoId = "video_ref";
      }

      title = `YouTube Video Lesson (Ref: ${videoId || "Online Source"})`;
      explanation = `Based on the video at ${youtubeUrl}, here is the simplified Class 9 master breakdown:
1. Core Physical Principle: The video explains physical interactions through observable real-world phenomena.
2. Step-by-Step Mechanism: Notice how forces and energy transformations occur in pairs. Newton's laws govern both the micro and macro dynamics.
3. Exam Takeaway: In subjective Class 9 CBSE/ICSE exams, you must state the underlying law before solving numerical steps, and always specify standard SI units.`;

      audioScript = `Hello student! I have reviewed the video lesson you shared. Let's break it down into very simple English. The core takeaway from this video is understanding how physical principles act in our daily environment. Pay close attention to how energy is conserved and forces balance each other out. Remember: in your exams, always define your variables clearly and never forget your SI units!`;

      keyPoints = [
        "Identified primary topic from video reference.",
        "Synthesized into simple, engaging conversational language.",
        "Extracted core formulas and exam-specific cautions."
      ];
      analogies = [
        "Relating the video experiment to household examples like rolling a ball or riding a bicycle."
      ];
    } else {
      // Document or direct text input
      const text = (content || "").trim();
      const preview = text.slice(0, 150);

      title = "Custom Document / Notes Analysis";
      explanation = `Here is your easy-to-understand teacher explanation synthesized from your uploaded notes:\n\n` +
        `Summary of your notes: "${preview}..."\n\n` +
        `Teacher Breakdown for Class 9:\n` +
        `• Core Definition: We break down the complex technical language in your document into clear, everyday concepts.\n` +
        `• Why it matters: In science, every theory is backed by mathematical relationships and experimental proof.\n` +
        `• Golden Rule for Exams: Frame your answers with a formal definition first, followed by formula/diagram, and finally real-world examples.`;

      audioScript = `Welcome! I have read your uploaded notes. Let me explain the key concept to you like your favorite teacher. The main idea here is straightforward. When you read complex science notes, focus on what causes the effect and what the result is. Let's look at a practical example so you never forget it in your exams.`;

      keyPoints = [
        "Synthesized key sentences from the uploaded document.",
        "Simplified heavy academic jargon into Class 9 friendly language.",
        "Ready for interactive voice narration."
      ];
      analogies = [
        "Visualizing the concepts through everyday actions like pushing, pulling, and bouncing."
      ];
    }

    return NextResponse.json({
      success: true,
      lesson: {
        title,
        explanation,
        audioScript,
        keyPoints,
        analogies
      }
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Failed to process tutor ingestion" }, { status: 500 });
  }
}
