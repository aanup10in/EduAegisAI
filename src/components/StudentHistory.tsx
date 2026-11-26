"use client";

import React, { useState, useEffect } from "react";
import {
  FileText,
  Clock,
  CheckCircle2,
  AlertTriangle,
  ShieldCheck,
  ChevronRight,
  RefreshCw,
  Award
} from "lucide-react";
import { SubjectiveSubmission } from "@/lib/storage";

interface StudentHistoryProps {
  onSelectSubmission: (sub: SubjectiveSubmission) => void;
  onNavigateToGrader: () => void;
}

export const StudentHistory: React.FC<StudentHistoryProps> = ({
  onSelectSubmission,
  onNavigateToGrader
}) => {
  const [submissions, setSubmissions] = useState<SubjectiveSubmission[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchHistory = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/teacher");
      const data = await res.json();
      setSubmissions(data.submissions || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">
            Student Academic Portfolio
          </span>
          <h2 className="text-xl font-black text-slate-900 mt-0.5">
            Evaluated Submissions & Academic Appeals
          </h2>
          <p className="text-xs text-slate-500">
            View your step-by-step graded subjective papers, verified teacher remarks, and appeal challenge statuses.
          </p>
        </div>

        <button
          onClick={fetchHistory}
          className="px-3.5 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-bold text-slate-700 flex items-center space-x-1.5 transition"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span>Refresh Records</span>
        </button>
      </div>

      {submissions.length === 0 ? (
        <div className="p-12 bg-white rounded-3xl border border-slate-200 text-center space-y-3">
          <div className="w-12 h-12 bg-indigo-50 rounded-2xl flex items-center justify-center mx-auto text-indigo-600 font-bold">
            <Award className="w-6 h-6" />
          </div>
          <h3 className="text-sm font-bold text-slate-900">No Assessment Records Found</h3>
          <p className="text-xs text-slate-500 max-w-sm mx-auto">
            You haven't submitted any subjective papers yet. Start your practice to receive audited AI feedback!
          </p>
          <button
            onClick={onNavigateToGrader}
            className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow transition"
          >
            Take 5-Question Practice Paper ➔
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {submissions.map((sub) => {
            const isPending = sub.status === "PENDING_TEACHER_RELEASE";
            const isReleased = sub.status === "RELEASED";
            const isAccepted = sub.status === "ACCEPTED";
            const isChallenged = sub.status === "CHALLENGED";

            return (
              <div
                key={sub.id}
                onClick={() => onSelectSubmission(sub)}
                className="bg-white p-5 rounded-3xl border border-slate-200 hover:border-indigo-300 shadow-sm hover:shadow-md transition cursor-pointer space-y-3"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-[10px] font-bold text-indigo-600 uppercase tracking-wider">
                      {sub.subjectName}
                    </span>
                    <h3 className="text-sm font-bold text-slate-900 mt-0.5">
                      {sub.chapterTitle}
                    </h3>
                    <p className="text-[11px] text-slate-500">
                      {new Date(sub.submittedAt).toLocaleDateString()} • {sub.board}
                    </p>
                  </div>

                  <div className="text-right">
                    <div className="text-base font-black text-indigo-600">
                      {sub.totalAwardedMarks} / {sub.totalMaxMarks}
                    </div>
                    <div className="text-[10px] font-semibold text-slate-400">Total Marks</div>
                  </div>
                </div>

                <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                  {isPending && (
                    <span className="font-bold text-amber-700 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200 flex items-center space-x-1 text-[11px]">
                      <Clock className="w-3 h-3" />
                      <span>Pending Teacher Release</span>
                    </span>
                  )}
                  {isReleased && (
                    <span className="font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200 flex items-center space-x-1 text-[11px]">
                      <ShieldCheck className="w-3 h-3" />
                      <span>Scores Released (Ready for Review)</span>
                    </span>
                  )}
                  {isAccepted && (
                    <span className="font-bold text-blue-700 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200 flex items-center space-x-1 text-[11px]">
                      <CheckCircle2 className="w-3 h-3" />
                      <span>Accepted Final Score</span>
                    </span>
                  )}
                  {isChallenged && (
                    <span className="font-bold text-rose-700 bg-rose-50 px-2.5 py-1 rounded-full border border-rose-200 flex items-center space-x-1 text-[11px]">
                      <AlertTriangle className="w-3 h-3" />
                      <span>Challenged by Student</span>
                    </span>
                  )}

                  <span className="text-indigo-600 font-bold flex items-center space-x-0.5">
                    <span>View Breakdown</span>
                    <ChevronRight className="w-4 h-4" />
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
