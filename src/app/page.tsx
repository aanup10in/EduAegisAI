"use client";

import React, { useState, useEffect } from "react";
import { Navbar } from "@/components/Navbar";
import { LoginModal } from "@/components/LoginModal";
import { AITutor } from "@/components/AITutor";
import { Grader } from "@/components/Grader";
import { SubmissionReview } from "@/components/SubmissionReview";
import { TeacherPanel } from "@/components/TeacherPanel";
import { StudentHistory } from "@/components/StudentHistory";
import { StudentProfile, SubjectiveSubmission } from "@/lib/storage";
import {
  GraduationCap,
  Sparkles,
  BookOpen,
  CheckCircle2,
  Shield,
  Layers,
  Sliders,
  ArrowRight
} from "lucide-react";

export default function Home() {
  // Navigation & User State
  const [currentBoard, setCurrentBoard] = useState<string>("CBSE (All India)");
  const [activeTab, setActiveTab] = useState<"tutor" | "grader" | "teacher" | "history">("tutor");
  const [userRole, setUserRole] = useState<"student" | "teacher">("student");

  // Profiles
  const [activeProfile, setActiveProfile] = useState<StudentProfile | null>(null);
  const [savedProfiles, setSavedProfiles] = useState<StudentProfile[]>([]);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

  // Active Graded Submission for Detailed View
  const [reviewedSubmission, setReviewedSubmission] = useState<SubjectiveSubmission | null>(null);
  const [targetChapterForGrader, setTargetChapterForGrader] = useState<string>("force_and_laws");

  // Load profiles on mount
  useEffect(() => {
    fetch("/api/auth")
      .then((res) => res.json())
      .then((data) => {
        if (data.students && data.students.length > 0) {
          setSavedProfiles(data.students);
          // Set first student as active by default
          setActiveProfile(data.students[0]);
          setCurrentBoard(data.students[0].board || "CBSE (All India)");
        } else {
          // Open onboarding for first-time user
          setIsLoginModalOpen(true);
        }
      })
      .catch((err) => {
        console.error("Auth fetch error:", err);
      });
  }, []);

  // Save new student profile
  const handleSaveProfile = async (profileData: any) => {
    const res = await fetch("/api/auth", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profileData)
    });
    const data = await res.json();
    if (data.profile) {
      setActiveProfile(data.profile);
      setCurrentBoard(data.profile.board);
      setSavedProfiles((prev) => [
        data.profile,
        ...prev.filter((p) => p.id !== data.profile.id)
      ]);
    }
  };

  // Switch to Grader directly from Tutor
  const handleNavigateToGraderFromTutor = (chapterId: string) => {
    setTargetChapterForGrader(chapterId);
    setReviewedSubmission(null);
    setActiveTab("grader");
  };

  // When submission completes
  const handleSubmissionComplete = (submission: SubjectiveSubmission) => {
    setReviewedSubmission(submission);
  };

  return (
    <div className="min-h-screen bg-slate-100/70 text-slate-900 flex flex-col font-sans">
      {/* Persistent Navbar with Global Board Selector */}
      <Navbar
        currentBoard={currentBoard}
        onBoardChange={(newBoard) => {
          setCurrentBoard(newBoard);
          if (activeProfile) {
            setActiveProfile({ ...activeProfile, board: newBoard });
          }
        }}
        activeProfile={activeProfile}
        onOpenLogin={() => setIsLoginModalOpen(true)}
        activeTab={activeTab}
        onTabChange={(tab) => {
          setActiveTab(tab);
          if (tab === "grader") {
            setReviewedSubmission(null);
          }
        }}
        userRole={userRole}
        onRoleToggle={(role) => setUserRole(role)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
        {/* Dual Primary Mode Selector Cards (1st: AI Tutor, 2nd: Grader) */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Card 1: AI Tutor */}
          <div
            onClick={() => {
              setActiveTab("tutor");
              setReviewedSubmission(null);
            }}
            className={`p-6 rounded-3xl border transition cursor-pointer flex items-center justify-between shadow-sm hover:shadow-md ${
              activeTab === "tutor"
                ? "bg-gradient-to-br from-indigo-900 via-indigo-950 to-slate-950 text-white border-indigo-700 ring-2 ring-indigo-500/30"
                : "bg-white hover:bg-slate-50 text-slate-800 border-slate-200"
            }`}
          >
            <div className="space-y-1">
              <span className={`text-[11px] font-bold uppercase tracking-wider ${activeTab === "tutor" ? "text-indigo-300" : "text-indigo-600"}`}>
                Module 1
              </span>
              <h2 className="text-xl font-black tracking-tight">1st — AI Tutor</h2>
              <p className={`text-xs ${activeTab === "tutor" ? "text-indigo-200" : "text-slate-500"} max-w-md`}>
                Socratic concept explanation, conversational audio teacher narration, multi-example mastery checks, and PDF/YouTube ingestion.
              </p>
            </div>
            <div className={`w-12 h-12 rounded-2xl flex items-center justify-center font-bold text-lg shrink-0 ${
              activeTab === "tutor" ? "bg-indigo-600 text-white shadow-lg" : "bg-indigo-50 text-indigo-600"
            }`}>
              <BookOpen className="w-6 h-6" />
            </div>
          </div>

          {/* Card 2: AI Grader */}
          <div
            onClick={() => {
              setActiveTab("grader");
              setReviewedSubmission(null);
            }}
            className={`p-6 rounded-3xl border transition cursor-pointer flex items-center justify-between shadow-sm hover:shadow-md ${
              activeTab === "grader" || reviewedSubmission
                ? "bg-gradient-to-br from-indigo-900 via-indigo-950 to-slate-950 text-white border-indigo-700 ring-2 ring-indigo-500/30"
                : "bg-white hover:bg-slate-50 text-slate-800 border-slate-200"
            }`}
          >
            <div className="space-y-1">
              <span className={`text-[11px] font-bold uppercase tracking-wider ${activeTab === "grader" ? "text-emerald-400" : "text-emerald-600"}`}>
                Module 2
              </span>
              <h2 className="text-xl font-black tracking-tight">2nd — AI Grader</h2>
              <p className={`text-xs ${activeTab === "grader" ? "text-indigo-200" : "text-slate-500"} max-w-md`}>
                Rubric-based subjective assessment, step-by-step mark explanations, teacher directives (edcafe.ai), and student appeal challenges.
              </p>
            </div>
            <div className={`w-12 h-12 rounded-2xl flex items-center justify-center font-bold text-lg shrink-0 ${
              activeTab === "grader" ? "bg-emerald-600 text-white shadow-lg" : "bg-emerald-50 text-emerald-600"
            }`}>
              <CheckCircle2 className="w-6 h-6" />
            </div>
          </div>
        </div>

        {/* Tab Content Display */}
        {activeTab === "tutor" && (
          <AITutor
            currentBoard={currentBoard}
            onNavigateToGrader={handleNavigateToGraderFromTutor}
          />
        )}

        {activeTab === "grader" && !reviewedSubmission && (
          <Grader
            currentBoard={currentBoard}
            onBoardChange={(newBoard) => setCurrentBoard(newBoard)}
            activeProfile={activeProfile}
            targetChapterId={targetChapterForGrader}
            onSubmissionComplete={handleSubmissionComplete}
            onOpenTeacherPanel={() => setActiveTab("teacher")}
          />
        )}

        {activeTab === "grader" && reviewedSubmission && (
          <div className="space-y-4">
            <button
              onClick={() => setReviewedSubmission(null)}
              className="text-xs font-bold text-indigo-600 hover:text-indigo-800 flex items-center space-x-1"
            >
              <span>← Back to Practice Questions</span>
            </button>
            <SubmissionReview
              submission={reviewedSubmission}
              onRefreshSubmission={() => {
                fetch("/api/teacher")
                  .then((res) => res.json())
                  .then((data) => {
                    const updated = data.submissions?.find((s: any) => s.id === reviewedSubmission.id);
                    if (updated) setReviewedSubmission(updated);
                  });
              }}
              onNavigateToTeacher={() => setActiveTab("teacher")}
            />
          </div>
        )}

        {activeTab === "history" && !reviewedSubmission && (
          <StudentHistory
            onSelectSubmission={(sub) => {
              setReviewedSubmission(sub);
              setActiveTab("grader");
            }}
            onNavigateToGrader={() => {
              setReviewedSubmission(null);
              setActiveTab("grader");
            }}
          />
        )}

        {activeTab === "teacher" && (
          <TeacherPanel
            onSelectSubmissionToReview={(sub) => {
              setReviewedSubmission(sub);
              setActiveTab("grader");
            }}
          />
        )}
      </main>

      {/* Footer */}
      <footer className="bg-slate-900 border-t border-slate-800 text-slate-400 py-6 text-xs text-center">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="flex items-center space-x-2">
            <Shield className="w-4 h-4 text-emerald-400" />
            <span className="font-bold text-white">EduAegis</span>
            <span>• Capstone Project for IIM Faculty Presentation</span>
          </div>
          <div>
            <span>Local Laptop Server & Vercel Ready • Compliant with Responsible AI Governance</span>
          </div>
        </div>
      </footer>

      {/* Onboarding / Login Modal */}
      <LoginModal
        isOpen={isLoginModalOpen}
        onClose={() => setIsLoginModalOpen(false)}
        activeProfile={activeProfile}
        savedProfiles={savedProfiles}
        onSelectProfile={(p) => {
          setActiveProfile(p);
          setCurrentBoard(p.board);
        }}
        onSaveNewProfile={handleSaveProfile}
      />
    </div>
  );
}
