"use client";

import React, { useState } from "react";
import { X, UserCheck, Sparkles, Building, Mail, Phone, MapPin, CheckCircle } from "lucide-react";
import { StudentProfile } from "@/lib/storage";
import { AVAILABLE_BOARDS } from "@/lib/curriculum";

interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
  activeProfile: StudentProfile | null;
  savedProfiles: StudentProfile[];
  onSelectProfile: (profile: StudentProfile) => void;
  onSaveNewProfile: (profileData: {
    name: string;
    studentClass: number;
    board: string;
    email: string;
    phone: string;
    cityState: string;
  }) => Promise<void>;
}

export const LoginModal: React.FC<LoginModalProps> = ({
  isOpen,
  onClose,
  activeProfile,
  savedProfiles,
  onSelectProfile,
  onSaveNewProfile
}) => {
  const [name, setName] = useState(activeProfile?.name || "");
  const [studentClass, setStudentClass] = useState<number>(activeProfile?.studentClass || 9);
  const [board, setBoard] = useState(activeProfile?.board || "CBSE (All India)");
  const [email, setEmail] = useState(activeProfile?.email || "");
  const [phone, setPhone] = useState(activeProfile?.phone || "");
  const [cityState, setCityState] = useState(activeProfile?.cityState || "Bangalore, Karnataka");
  const [loading, setLoading] = useState(false);
  const [tab, setTab] = useState<"register" | "saved">("register");

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !email) {
      alert("Please provide at least your Name and Email ID.");
      return;
    }
    setLoading(true);
    try {
      await onSaveNewProfile({
        name,
        studentClass,
        board,
        email,
        phone,
        cityState
      });
      onClose();
    } catch (err: any) {
      alert(err.message || "Failed to save profile.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="relative w-full max-w-lg bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden">
        {/* Modal Header */}
        <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-6 text-white">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2.5">
              <div className="w-9 h-9 rounded-xl bg-indigo-500/30 flex items-center justify-center text-indigo-300 font-bold border border-indigo-500/40">
                🛡️
              </div>
              <div>
                <h3 className="text-lg font-bold">EduAegis Student Access</h3>
                <p className="text-xs text-indigo-200">First-time Onboarding & Profile Verification</p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="p-1.5 rounded-full hover:bg-white/10 text-slate-300 transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Tab Switcher if there are saved profiles */}
          {savedProfiles.length > 0 && (
            <div className="flex space-x-2 mt-4 bg-slate-800/60 p-1 rounded-xl">
              <button
                type="button"
                onClick={() => setTab("register")}
                className={`flex-1 py-1.5 text-xs font-semibold rounded-lg transition ${
                  tab === "register" ? "bg-indigo-600 text-white" : "text-slate-400 hover:text-white"
                }`}
              >
                {activeProfile ? "Edit Active Profile" : "Register / Sign In"}
              </button>
              <button
                type="button"
                onClick={() => setTab("saved")}
                className={`flex-1 py-1.5 text-xs font-semibold rounded-lg transition ${
                  tab === "saved" ? "bg-indigo-600 text-white" : "text-slate-400 hover:text-white"
                }`}
              >
                Switch Account ({savedProfiles.length})
              </button>
            </div>
          )}
        </div>

        {tab === "saved" ? (
          <div className="p-6 space-y-3 max-h-[420px] overflow-y-auto">
            <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">
              Saved Students on Local Server
            </div>
            {savedProfiles.map((p) => (
              <div
                key={p.id}
                onClick={() => {
                  onSelectProfile(p);
                  onClose();
                }}
                className={`p-3.5 rounded-2xl border transition cursor-pointer flex items-center justify-between ${
                  activeProfile?.id === p.id
                    ? "bg-indigo-50 border-indigo-400 shadow-sm"
                    : "bg-slate-50 hover:bg-slate-100 border-slate-200"
                }`}
              >
                <div className="flex items-center space-x-3">
                  <div className="w-9 h-9 rounded-xl bg-indigo-600 text-white font-bold text-sm flex items-center justify-center">
                    {p.name.charAt(0)}
                  </div>
                  <div>
                    <h4 className="text-sm font-bold text-slate-900">{p.name}</h4>
                    <p className="text-xs text-slate-500">
                      Class {p.studentClass}th • {p.board} • {p.cityState}
                    </p>
                  </div>
                </div>
                {activeProfile?.id === p.id && (
                  <span className="text-xs font-bold text-indigo-700 bg-indigo-100 px-2 py-0.5 rounded-full flex items-center space-x-1">
                    <CheckCircle className="w-3.5 h-3.5" />
                    <span>Active</span>
                  </span>
                )}
              </div>
            ))}
            <button
              onClick={() => {
                setName("");
                setEmail("");
                setPhone("");
                setTab("register");
              }}
              className="w-full mt-3 py-2.5 border border-dashed border-indigo-300 text-indigo-600 font-semibold rounded-xl text-xs hover:bg-indigo-50 transition"
            >
              + Register Another Student
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="p-6 space-y-4">
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                Student Full Name *
              </label>
              <input
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="e.g. Aarav Sharma"
                className="w-full px-3.5 py-2.5 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition"
              />
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                  Class Standard
                </label>
                <select
                  value={studentClass}
                  onChange={(e) => setStudentClass(Number(e.target.value))}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 bg-white"
                >
                  <option value={8}>Class 8th</option>
                  <option value={9}>Class 9th (Active Prototype)</option>
                  <option value={10}>Class 10th</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                  Academic Board
                </label>
                <select
                  value={board}
                  onChange={(e) => setBoard(e.target.value)}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 bg-white"
                >
                  {AVAILABLE_BOARDS.map((b) => (
                    <option key={b.id} value={b.name}>
                      {b.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                Student / Parent Email ID *
              </label>
              <div className="relative">
                <Mail className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="aarav.sharma@school.edu"
                  className="w-full pl-10 pr-3.5 py-2.5 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                  Phone Number
                </label>
                <div className="relative">
                  <Phone className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                  <input
                    type="tel"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    placeholder="+91 98765 43210"
                    className="w-full pl-10 pr-3 py-2 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                  City & State
                </label>
                <div className="relative">
                  <MapPin className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
                  <input
                    type="text"
                    value={cityState}
                    onChange={(e) => setCityState(e.target.value)}
                    placeholder="Bangalore, Karnataka"
                    className="w-full pl-10 pr-3 py-2 text-sm border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                  />
                </div>
              </div>
            </div>

            <p className="text-[11px] text-slate-500 pt-1">
              🔒 Information is stored on your local laptop server and persisted across your study sessions.
            </p>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl shadow-lg shadow-indigo-600/30 transition flex items-center justify-center space-x-2"
            >
              <span>{loading ? "Saving Details..." : "Save & Continue to Learning"}</span>
            </button>
          </form>
        )}
      </div>
    </div>
  );
};
