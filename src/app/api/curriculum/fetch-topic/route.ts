import { NextResponse } from "next/server";
import { CURRICULUM_DATA, generateDynamicTopicContent, Chapter } from "@/lib/curriculum";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { topic, subject, studentClass, board } = body;

    const classNum = Number(studentClass) || 9;
    const cur = CURRICULUM_DATA[classNum] || CURRICULUM_DATA[9];
    const subObj = cur.subjects.find((s) => s.id === (subject || "physics")) || cur.subjects[0];

    // Check if the topic matches an existing chapter
    if (topic) {
      const topicLower = topic.toLowerCase().trim();
      for (const ch of subObj.chapters) {
        if (ch.title.toLowerCase().includes(topicLower) || topicLower.includes(ch.title.toLowerCase())) {
          return NextResponse.json({ success: true, chapter: ch, isDynamic: false });
        }
      }

      // If custom user-entered topic, dynamically generate rich content
      const dynamicChapter = generateDynamicTopicContent(
        topic,
        subObj.name,
        classNum,
        board || "CBSE (All India)"
      );
      return NextResponse.json({ success: true, chapter: dynamicChapter, isDynamic: true });
    }

    // Default to first chapter
    return NextResponse.json({
      success: true,
      chapter: subObj.chapters[0] || generateDynamicTopicContent("Fundamental Principles", subObj.name, classNum, board),
      isDynamic: false
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Failed to fetch topic content" }, { status: 500 });
  }
}
