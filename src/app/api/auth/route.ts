import { NextResponse } from "next/server";
import { getDatabase, saveDatabase, StudentProfile } from "@/lib/storage";

export async function GET() {
  const db = getDatabase();
  return NextResponse.json({
    students: db.students
  });
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { name, studentClass, board, email, phone, cityState } = body;

    if (!name || !email) {
      return NextResponse.json({ error: "Name and Email are required." }, { status: 400 });
    }

    const db = getDatabase();
    
    // Check if student already exists by email
    const existingIndex = db.students.findIndex(s => s.email.toLowerCase() === email.toLowerCase());

    let profile: StudentProfile;

    if (existingIndex >= 0) {
      // Update existing
      profile = {
        ...db.students[existingIndex],
        name,
        studentClass: Number(studentClass) || 9,
        board: board || db.students[existingIndex].board,
        phone: phone || db.students[existingIndex].phone,
        cityState: cityState || db.students[existingIndex].cityState,
        lastLoginAt: new Date().toISOString()
      };
      db.students[existingIndex] = profile;
    } else {
      // Create new profile
      profile = {
        id: "std_" + Date.now(),
        name,
        studentClass: Number(studentClass) || 9,
        board: board || "CBSE (All India)",
        email,
        phone: phone || "",
        cityState: cityState || "",
        createdAt: new Date().toISOString(),
        lastLoginAt: new Date().toISOString()
      };
      db.students.unshift(profile);
    }

    saveDatabase(db);
    return NextResponse.json({ success: true, profile });
  } catch (err: any) {
    return NextResponse.json({ error: err.message || "Failed to save profile" }, { status: 500 });
  }
}
