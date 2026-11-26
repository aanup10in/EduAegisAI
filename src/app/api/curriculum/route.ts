import { NextResponse } from "next/server";
import { CURRICULUM_DATA, AVAILABLE_BOARDS } from "@/lib/curriculum";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const classParam = searchParams.get("class");

  if (classParam) {
    const classNum = parseInt(classParam, 10);
    const classData = CURRICULUM_DATA[classNum];
    if (classData) {
      return NextResponse.json({ classData, boards: AVAILABLE_BOARDS });
    }
  }

  return NextResponse.json({
    curriculum: CURRICULUM_DATA,
    boards: AVAILABLE_BOARDS
  });
}
