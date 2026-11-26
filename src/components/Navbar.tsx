"use client";

import React, { useState } from "react";
import { Shield, GraduationCap, ChevronDown, User, LogOut, CheckCircle2, Sliders, Sparkles } from "lucide-react";
import { AVAILABLE_BOARDS } from "@/lib/curriculum";
import { StudentProfile } from "@/lib/storage";

interface NavbarProps {
  currentBoard: string;
  onBoardChange: (board: string) => void;
  activeProfile: StudentProfile | null;
  onOpenLogin: () => void;
  activeTab: "tutor" | "grader" | "teacher" | "history";
  onTabChange: (tab: "tutor" | "grader" | "teacher" | "history") => void;
  userRole: "student" | "teacher";
  onRoleToggle: (role: "student" | "teacher") => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentBoard,
  onBoardChange,
  activeProfile,
  onOpenLogin,
  activeTab,
  onTabChange,
  userRole,
  onRoleToggle
}) => {
  const [boardDropdownOpen, setBoardDropdownOpen] = useState(false);

  const activeBoardObj = AVAILABLE_BOARDS.find(b => b.name === currentBoard) || AVAILABLE_BOARDS[0];

  return (
    <header className="sticky top-0 z-50 bg-slate-900 border-b border-slate-800 text-white shadow-xl backdrop-blur-md bg-opacity-95">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Aegis Brand */}
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => onTabChange("tutor")}>
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-500 via-blue-600 to-emerald-400 p-0.5 shadow-lg shadow-indigo-500/30 flex items-center justify-center">
              <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
                <Shield className="w-5 h-5 text-emerald-400" />
              </div>
            </div>
            <div>
              <div className="flex items-center space-x-1.5">
                <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-white via-indigo-100 to-indigo-300 bg-clip-text text-transparent">
                  EduAegis
                </span>
                <span className="text-[10px] uppercase font-bold tracking-widest px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  AI Tutor & Grader
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium hidden sm:block">
                Responsible AI & Subjective Evaluation Governance
              </p>
            </div>
          </div>

          {/* Persistent Board Selector Pill (Always Visible on Top of Every Page) */}
          <div className="relative">
            <button
              onClick={() => setBoardDropdownOpen(!boardDropdownOpen)}
              className="flex items-center space-x-2 px-3 py-1.5 rounded-full bg-indigo-950/80 border border-indigo-700/60 hover:border-indigo-500 text-xs text-indigo-200 transition shadow-inner"
              title="Change Academic Curriculum Board"
            >
              <GraduationCap className="w-3.5 h-3.5 text-indigo-400" />
              <span className="font-semibold text-slate-200 hidden md:inline">Board:</span>
              <span className="font-bold text-white bg-indigo-600/60 px-2 py-0.5 rounded-full text-[11px]">
                {activeBoardObj.name.split(" ")[0]}
              </span>
              <ChevronDown className="w-3 h-3 text-slate-400" />
            </button>

            {boardDropdownOpen && (
              <div className="absolute right-0 mt-2 w-72 bg-slate-900 border border-slate-700 rounded-xl shadow-2xl p-2 z-50 animate-in fade-in zoom-in-95">
                <div className="px-3 py-1.5 border-b border-slate-800 text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                  Select Curriculum Board
                </div>
                {AVAILABLE_BOARDS.map((board) => (
                  <button
                    key={board.id}
                    onClick={() => {
                      onBoardChange(board.name);
                      setBoardDropdownOpen(false);
                    }}
                    className={`w-full text-left px-3 py-2 rounded-lg text-xs font-medium flex items-center justify-between transition mt-1 ${
                      currentBoard === board.name
                        ? "bg-indigo-600 text-white"
                        : "text-slate-300 hover:bg-slate-800 hover:text-white"
                    }`}
                  >
                    <span>{board.name}</span>
                    {currentBoard === board.name && <CheckCircle2 className="w-4 h-4 text-emerald-300" />}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Navigation Tabs (AI Tutor, Grader, Submissions, Teacher) */}
          <nav className="hidden lg:flex items-center space-x-1 bg-slate-950/60 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => onTabChange("tutor")}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
                activeTab === "tutor"
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/30"
                  : "text-slate-400 hover:text-white hover:bg-slate-800/60"
              }`}
            >
              1. AI Tutor
            </button>
            <button
              onClick={() => onTabChange("grader")}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
                activeTab === "grader"
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/30"
                  : "text-slate-400 hover:text-white hover:bg-slate-800/60"
              }`}
            >
              2. AI Grader
            </button>
            <button
              onClick={() => onTabChange("history")}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
                activeTab === "history"
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/30"
                  : "text-slate-400 hover:text-white hover:bg-slate-800/60"
              }`}
            >
              My Evaluations & Appeals
            </button>
            <button
              onClick={() => onTabChange("teacher")}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center space-x-1.5 transition ${
                activeTab === "teacher"
                  ? "bg-amber-600 text-white shadow-md shadow-amber-600/30"
                  : "text-amber-400 hover:text-amber-300 hover:bg-slate-800/60"
              }`}
            >
              <Sliders className="w-3.5 h-3.5" />
              <span>Teacher / Governance Panel</span>
            </button>
          </nav>

          {/* User Profile & Role Switcher */}
          <div className="flex items-center space-x-3">
            {activeProfile ? (
              <div
                onClick={onOpenLogin}
                className="flex items-center space-x-2.5 px-3 py-1.5 rounded-xl bg-slate-800/90 border border-slate-700 hover:border-slate-600 cursor-pointer transition"
                title="Click to view or switch profile"
              >
                <div className="w-7 h-7 rounded-lg bg-indigo-500/30 text-indigo-300 font-bold text-xs flex items-center justify-center border border-indigo-400/40">
                  {activeProfile.name.charAt(0)}
                </div>
                <div className="text-left hidden sm:block">
                  <div className="text-xs font-bold text-slate-200 leading-tight">
                    {activeProfile.name}
                  </div>
                  <div className="text-[10px] text-slate-400">
                    Class {activeProfile.studentClass}th • {activeProfile.cityState.split(",")[0] || "CBSE"}
                  </div>
                </div>
              </div>
            ) : (
              <button
                onClick={onOpenLogin}
                className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold transition shadow"
              >
                Sign In
              </button>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};
