import fs from "fs";
import path from "path";

export interface StudentProfile {
  id: string;
  name: string;
  studentClass: number; // 8, 9, 10
  board: string;
  email: string;
  phone: string;
  cityState: string;
  createdAt: string;
  lastLoginAt: string;
}

export interface TeacherInstruction {
  id: string;
  topicId: string;
  specificInstructions: string;
  strictSIUnits: boolean;
  partialCreditForSteps: boolean;
  lenientSpelling: boolean;
  weights: {
    facts: number;
    concepts: number;
    terminology: number;
    derivation: number;
  };
  updatedAt: string;
}

export interface StepEvaluation {
  stepNumber: number;
  stepFocus: string;
  marksAwarded: number;
  maxMarks: number;
  whyAwardedOrDeducted: string;
}

export interface QuestionGrading {
  questionId: string;
  questionText: string;
  studentAnswer: string;
  maxMarks: number;
  awardedMarks: number;
  teacherOverrideMarks?: number;
  stepBreakdown: StepEvaluation[];
  strengths: string[];
  gapsAndMisconceptions: string[];
  deductionExplanation: string;
  referenceChapter: string;
  authenticReferences: { title: string; url: string; source: string }[];
  isChallenged?: boolean;
  studentChallengeReason?: string;
  teacherChallengeResolution?: string;
}

export interface SubjectiveSubmission {
  id: string;
  studentId: string;
  studentName: string;
  board: string;
  className: string;
  subjectName: string;
  chapterTitle: string;
  topicName: string;
  submittedAt: string;
  totalMaxMarks: number;
  totalAwardedMarks: number;
  status: "PENDING_TEACHER_RELEASE" | "RELEASED" | "ACCEPTED" | "CHALLENGED";
  teacherInstructionsUsed: string;
  questions: QuestionGrading[];
  teacherOverallFeedback?: string;
  releasedAt?: string;
  acceptedAt?: string;
  challengedAt?: string;
}

export interface EduAegisDatabase {
  students: StudentProfile[];
  teacherInstructions: Record<string, TeacherInstruction>;
  submissions: SubjectiveSubmission[];
}

const DB_FILE_PATH = path.join(process.cwd(), "eduaegis_data.json");

// Default initial dataset
const INITIAL_DATABASE: EduAegisDatabase = {
  students: [
    {
      id: "std_default_aarav",
      name: "Aarav Sharma",
      studentClass: 9,
      board: "CBSE (All India)",
      email: "aarav.sharma@school.edu",
      phone: "+91 98765 43210",
      cityState: "Bangalore, Karnataka",
      createdAt: new Date().toISOString(),
      lastLoginAt: new Date().toISOString()
    },
    {
      id: "std_priya",
      name: "Priya Patel",
      studentClass: 9,
      board: "ICSE / CISCE",
      email: "priya.patel@icse.org",
      phone: "+91 91234 56789",
      cityState: "Ahmedabad, Gujarat",
      createdAt: new Date().toISOString(),
      lastLoginAt: new Date().toISOString()
    }
  ],
  teacherInstructions: {
    force_and_laws: {
      id: "instr_1",
      topicId: "force_and_laws",
      specificInstructions: "Focus strictly on proper statement of Newton's 2nd Law (rate of change of momentum). Penalize 0.5 marks if SI units (N, kg, m/s²) are omitted. Allow partial marks for mathematical derivation steps.",
      strictSIUnits: true,
      partialCreditForSteps: true,
      lenientSpelling: true,
      weights: {
        facts: 0.3,
        concepts: 0.4,
        terminology: 0.2,
        derivation: 0.1
      },
      updatedAt: new Date().toISOString()
    }
  },
  submissions: []
};

// In-memory cache for serverless environments (Vercel) & local speeds
let memoryDb: EduAegisDatabase | null = null;

export function getDatabase(): EduAegisDatabase {
  if (memoryDb) {
    return memoryDb;
  }

  try {
    if (fs.existsSync(DB_FILE_PATH)) {
      const content = fs.readFileSync(DB_FILE_PATH, "utf-8");
      memoryDb = JSON.parse(content);
      return memoryDb!;
    }
  } catch (err) {
    console.warn("Could not read local DB file, initializing with in-memory store:", err);
  }

  memoryDb = JSON.parse(JSON.stringify(INITIAL_DATABASE));
  saveDatabase(memoryDb!);
  return memoryDb!;
}

export function saveDatabase(data: EduAegisDatabase): void {
  memoryDb = data;
  try {
    fs.writeFileSync(DB_FILE_PATH, JSON.stringify(data, null, 2), "utf-8");
  } catch (err) {
    // Vercel serverless functions have a read-only filesystem except /tmp; gracefully handle it
    console.warn("Notice: File write skipped in read-only environment; memory cache preserved.");
  }
}
