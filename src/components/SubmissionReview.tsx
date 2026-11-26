"use client";

import React, { useState } from "react";
import {
  ShieldCheck,
  Clock,
  CheckCircle2,
  AlertCircle,
  ThumbsUp,
  AlertTriangle,
  ExternalLink,
  BookOpen,
  ArrowRight,
  FileCheck,
  Send,
  MessageSquare,
  HelpCircle
} from "lucide-react";
import { SubjectiveSubmission } from "@/lib/storage";

interface SubmissionReviewProps {
  submission: SubjectiveSubmission;
  onRefreshSubmission: () => void;
  onNavigateToTeacher: () => void;
}

export const SubmissionReview: React.FC<SubmissionReviewProps> = ({
  submission,
  onRefreshSubmission,
  onNavigateToTeacher
}) => {
  // Challenge modal state
  const [isChallengeModalOpen, setIsChallengeModalOpen] = useState(false);
  const [selectedQuestionsToChallenge, setSelectedQuestionsToChallenge] = useState<Record<string, boolean>>({});
  const [challengeReasons, setChallengeReasons] = useState<Record<string, string>>({});
  const [isSubmittingDecision, setIsSubmittingDecision] = useState(false);

  const isPending = submission.status === "PENDING_TEACHER_RELEASE";
  const isReleased = submission.status === "RELEASED";
  const isAccepted = submission.status === "ACCEPTED";
  const isChallenged = submission.status === "CHALLENGED";

  // Handle "I Accept"
  const handleAccept = async () => {
    if (!confirm("Are you sure you want to accept these evaluated scores? This will finalize your marks.")) {
      return;
    }
    setIsSubmittingDecision(true);
    try {
      const res = await fetch("/api/student/challenge", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          submissionId: submission.id,
          decision: "ACCEPT"
        })
      });
      const data = await res.json();
      if (data.success) {
        alert("Scores Accepted! Your verified result has been recorded in your academic profile.");
        onRefreshSubmission();
      }
    } catch (err: any) {
      alert("Failed to accept score: " + err.message);
    } finally {
      setIsSubmittingDecision(false);
    }
  };

  // Open Challenge Modal
  const openChallengeModal = () => {
    // initialize selected questions
    const initialSelection: Record<string, boolean> = {};
    const initialReasons: Record<string, string> = {};
    submission.questions.forEach((q) => {
      initialSelection[q.questionId] = false;
      initialReasons[q.questionId] = "";
    });
    setSelectedQuestionsToChallenge(initialSelection);
    setChallengeReasons(initialReasons);
    setIsChallengeModalOpen(true);
  };

  // Submit Challenge
  const handleSubmitChallenge = async () => {
    const questionsToChallenge = Object.entries(selectedQuestionsToChallenge)
      .filter(([_, isSelected]) => isSelected)
      .map(([qId]) => ({
        questionId: qId,
        reason: challengeReasons[qId] || "Student requested step-by-step re-check."
      }));

    if (questionsToChallenge.length === 0) {
      alert("Please select at least one question you wish to challenge.");
      return;
    }

    // Ensure reasons are entered
    for (const item of questionsToChallenge) {
      if (!item.reason.trim()) {
        alert("Please write your specific justification for each challenged question.");
        return;
      }
    }

    setIsSubmittingDecision(true);
    try {
      const res = await fetch("/api/student/challenge", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          submissionId: submission.id,
          decision: "CHALLENGE",
          challenges: questionsToChallenge
        })
      });
      const data = await res.json();
      if (data.success) {
        alert("Your challenge has been submitted to the Subject Teacher for re-evaluation.");
        setIsChallengeModalOpen(false);
        onRefreshSubmission();
      }
    } catch (err: any) {
      alert("Failed to submit challenge: " + err.message);
    } finally {
      setIsSubmittingDecision(false);
    }
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Top Evaluation Status Card */}
      <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">
                Assessment Record
              </span>
              <span>•</span>
              <span className="text-xs text-slate-500 font-medium">
                {new Date(submission.submittedAt).toLocaleDateString()}
              </span>
            </div>
            <h2 className="text-xl font-black text-slate-900 mt-0.5">
              {submission.chapterTitle} ({submission.subjectName})
            </h2>
            <p className="text-xs text-slate-500">
              Candidate: <strong>{submission.studentName}</strong> • {submission.board} • {submission.className}
            </p>
          </div>

          {/* Status Badge */}
          <div className="text-right">
            {isPending && (
              <div className="flex items-center space-x-2 bg-amber-50 border border-amber-200 px-3.5 py-1.5 rounded-full text-amber-800 text-xs font-bold">
                <Clock className="w-4 h-4 animate-spin" />
                <span>Pending Teacher Audit & Release</span>
              </div>
            )}
            {isReleased && (
              <div className="flex items-center space-x-2 bg-emerald-50 border border-emerald-300 px-3.5 py-1.5 rounded-full text-emerald-800 text-xs font-bold">
                <ShieldCheck className="w-4 h-4 text-emerald-600" />
                <span>Scores Officially Released</span>
              </div>
            )}
            {isAccepted && (
              <div className="flex items-center space-x-2 bg-blue-50 border border-blue-200 px-3.5 py-1.5 rounded-full text-blue-800 text-xs font-bold">
                <CheckCircle2 className="w-4 h-4 text-blue-600" />
                <span>Marks Accepted by Student</span>
              </div>
            )}
            {isChallenged && (
              <div className="flex items-center space-x-2 bg-rose-50 border border-rose-200 px-3.5 py-1.5 rounded-full text-rose-800 text-xs font-bold">
                <AlertTriangle className="w-4 h-4 text-rose-600" />
                <span>Under Teacher Re-Evaluation (Challenged)</span>
              </div>
            )}
            <div className="text-xs text-slate-500 mt-1">
              Score: <strong className="text-slate-900 text-sm">{submission.totalAwardedMarks}</strong> / {submission.totalMaxMarks} Marks
            </div>
          </div>
        </div>

        {/* AI Governance Notice */}
        {isPending && (
          <div className="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-amber-900 space-y-2">
            <div className="flex items-center space-x-2 font-bold text-xs">
              <AlertCircle className="w-4 h-4 text-amber-600" />
              <span>AI Governance & Human-in-the-Loop Protocol Active:</span>
            </div>
            <p className="text-xs leading-relaxed">
              EduAegis has completed AI rubric checking. To prevent unfair automated grading, the AI cannot unilaterally publish final marks.
              Your Subject Teacher is currently reviewing the step-by-step scoring.
            </p>
            <div className="pt-1">
              <button
                onClick={onNavigateToTeacher}
                className="px-3.5 py-1.5 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-bold transition shadow-sm"
              >
                Go to Teacher Panel to Audit & Release Marks ➔
              </button>
            </div>
          </div>
        )}

        {/* Teacher Feedback Banner if provided */}
        {submission.teacherOverallFeedback && (
          <div className="p-3.5 rounded-2xl bg-indigo-50 border border-indigo-200 text-xs text-indigo-950 space-y-1">
            <span className="font-bold">Teacher Feedback:</span>
            <p className="text-slate-700">{submission.teacherOverallFeedback}</p>
          </div>
        )}
      </div>

      {/* Step-by-Step Question Breakdown */}
      <div className="space-y-4">
        <h3 className="text-base font-black text-slate-900 flex items-center justify-between">
          <span>Detailed Step-by-Step Scoring & Explanations</span>
          <span className="text-xs font-normal text-slate-500">
            Every step shows why marks were awarded or deducted
          </span>
        </h3>

        {submission.questions.map((q, idx) => (
          <div
            key={q.questionId}
            className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4"
          >
            {/* Question Header & Score */}
            <div className="flex items-start justify-between gap-4 border-b border-slate-100 pb-3">
              <div className="space-y-1">
                <span className="text-[11px] font-bold text-indigo-600 uppercase tracking-wider">
                  Question {idx + 1}
                </span>
                <h4 className="text-xs font-bold text-slate-900 leading-relaxed">
                  {q.questionText}
                </h4>
              </div>

              <div className="text-right shrink-0">
                <div className="text-base font-black text-indigo-600">
                  {q.teacherOverrideMarks ?? q.awardedMarks} / {q.maxMarks}
                </div>
                {q.teacherOverrideMarks !== undefined && (
                  <span className="text-[10px] font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded-full">
                    Teacher Adjusted
                  </span>
                )}
                {q.isChallenged && (
                  <span className="text-[10px] font-bold text-rose-700 bg-rose-100 px-2 py-0.5 rounded-full block mt-0.5">
                    Challenged by Student
                  </span>
                )}
              </div>
            </div>

            {/* Student's Answer */}
            <div className="space-y-1">
              <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                Student's Submitted Answer:
              </span>
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs font-mono text-slate-800 whitespace-pre-wrap leading-relaxed">
                {q.studentAnswer || "No answer provided."}
              </div>
            </div>

            {/* Step-by-Step Scoring Breakdown (Explanation of Every Step) */}
            <div className="space-y-2">
              <span className="text-[10px] font-bold text-slate-700 uppercase tracking-wider flex items-center space-x-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                <span>Step-by-Step Rubric Audit Trail:</span>
              </span>

              <div className="space-y-1.5">
                {q.stepBreakdown.map((st) => (
                  <div
                    key={st.stepNumber}
                    className="p-3 rounded-xl border border-slate-200 bg-slate-50/70 text-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2"
                  >
                    <div>
                      <strong className="text-indigo-900">Step {st.stepNumber} ({st.stepFocus}):</strong>
                      <p className="text-slate-600 mt-0.5">{st.whyAwardedOrDeducted}</p>
                    </div>

                    <span
                      className={`px-2.5 py-1 rounded-lg text-xs font-bold shrink-0 ${
                        st.marksAwarded === st.maxMarks
                          ? "bg-emerald-100 text-emerald-800"
                          : st.marksAwarded > 0
                          ? "bg-amber-100 text-amber-800"
                          : "bg-rose-100 text-rose-800"
                      }`}
                    >
                      {st.marksAwarded} / {st.maxMarks} Marks
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Deductions & Misconceptions Rationale */}
            {q.gapsAndMisconceptions.length > 0 && (
              <div className="p-3 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-900 space-y-1">
                <strong className="flex items-center space-x-1 text-rose-700">
                  <AlertCircle className="w-3.5 h-3.5" />
                  <span>Deductions & Misconceptions Rationale:</span>
                </strong>
                <ul className="list-disc list-inside space-y-0.5 text-[11px] text-rose-800">
                  {q.gapsAndMisconceptions.map((g, i) => (
                    <li key={i}>{g}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Authentic Website References & Chapter Citation */}
            <div className="pt-2 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-[11px]">
              <span className="text-slate-500">
                📘 Reference Chapter: <strong>{q.referenceChapter}</strong>
              </span>

              <div className="flex flex-wrap gap-2">
                {q.authenticReferences.map((ref, i) => (
                  <a
                    key={i}
                    href={ref.url}
                    target="_blank"
                    rel="noreferrer"
                    className="text-indigo-600 hover:text-indigo-800 underline flex items-center space-x-1"
                  >
                    <span>{ref.title}</span>
                    <ExternalLink className="w-3 h-3" />
                  </a>
                ))}
              </div>
            </div>

            {/* Display Challenge Reason & Resolution if present */}
            {q.studentChallengeReason && (
              <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900 space-y-1">
                <span className="font-bold">Student's Challenge Reason:</span>
                <p className="text-slate-800 italic">"{q.studentChallengeReason}"</p>
                {q.teacherChallengeResolution && (
                  <div className="mt-2 pt-2 border-t border-amber-200">
                    <span className="font-bold text-emerald-800">Teacher Resolution Remark:</span>
                    <p className="text-slate-700">{q.teacherChallengeResolution}</p>
                  </div>
                )}
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Part 3: Acceptance & Challenge Footer (As Requested in Prompt) */}
      {isReleased && (
        <div className="sticky bottom-4 z-40 bg-slate-900 p-5 rounded-3xl shadow-2xl border border-slate-800 text-white flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <div className="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center space-x-1.5">
              <ShieldCheck className="w-4 h-4" />
              <span>Verified Scores Released by Teacher</span>
            </div>
            <p className="text-xs text-slate-300 mt-0.5">
              Please review the line-by-line mark breakdown. Do you accept these scores or wish to submit an academic challenge?
            </p>
          </div>

          <div className="flex items-center space-x-3 w-full sm:w-auto">
            {/* Option 1: I Accept */}
            <button
              onClick={handleAccept}
              disabled={isSubmittingDecision}
              className="flex-1 sm:flex-initial px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs rounded-xl shadow-lg transition flex items-center justify-center space-x-1.5"
            >
              <CheckCircle2 className="w-4 h-4" />
              <span>1 - I Accept</span>
            </button>

            {/* Option 2: I Challenge */}
            <button
              onClick={openChallengeModal}
              disabled={isSubmittingDecision}
              className="flex-1 sm:flex-initial px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-xs rounded-xl shadow-lg transition flex items-center justify-center space-x-1.5"
            >
              <AlertTriangle className="w-4 h-4" />
              <span>2 - I Challenge</span>
            </button>
          </div>
        </div>
      )}

      {/* Accepted State Notification */}
      {isAccepted && (
        <div className="p-5 rounded-3xl bg-blue-50 border border-blue-200 text-blue-950 flex items-center justify-between">
          <div>
            <div className="text-xs font-bold text-blue-700 uppercase tracking-wider">
              Score Acceptance Finalized
            </div>
            <p className="text-xs text-slate-600 mt-0.5">
              You accepted your final score of {submission.totalAwardedMarks} / {submission.totalMaxMarks}.
              Archived in academic records on {new Date(submission.acceptedAt || Date.now()).toLocaleString()}.
            </p>
          </div>
          <CheckCircle2 className="w-8 h-8 text-blue-600 shrink-0" />
        </div>
      )}

      {/* Challenge Modal */}
      {isChallengeModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
          <div className="relative w-full max-w-2xl bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden max-h-[90vh] flex flex-col">
            <div className="bg-gradient-to-r from-slate-900 to-indigo-950 p-6 text-white shrink-0">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="text-lg font-bold">Academic Challenge & Re-Evaluation</h3>
                  <p className="text-xs text-indigo-200">
                    Select specific questions and write your clear justification for teacher review
                  </p>
                </div>
                <button
                  onClick={() => setIsChallengeModalOpen(false)}
                  className="text-slate-400 hover:text-white"
                >
                  ✕
                </button>
              </div>
            </div>

            <div className="p-6 space-y-4 overflow-y-auto">
              <p className="text-xs text-slate-600 leading-relaxed">
                Under EduAegis governance policies, students and parents hold the right to challenge automated or manual grading.
                Please select the question(s) you wish to appeal and write your specific reasons:
              </p>

              {submission.questions.map((q, idx) => {
                const isSelected = selectedQuestionsToChallenge[q.questionId] || false;
                return (
                  <div
                    key={q.questionId}
                    className={`p-4 rounded-2xl border transition space-y-2 ${
                      isSelected
                        ? "bg-amber-50/70 border-amber-300"
                        : "bg-slate-50 border-slate-200"
                    }`}
                  >
                    <label className="flex items-start space-x-3 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={isSelected}
                        onChange={(e) =>
                          setSelectedQuestionsToChallenge((prev) => ({
                            ...prev,
                            [q.questionId]: e.target.checked
                          }))
                        }
                        className="mt-1 w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500"
                      />
                      <div>
                        <div className="text-xs font-bold text-slate-900">
                          Question {idx + 1}: {q.questionText}
                        </div>
                        <div className="text-[11px] text-slate-500">
                          Current Score: {q.teacherOverrideMarks ?? q.awardedMarks} / {q.maxMarks} Marks
                        </div>
                      </div>
                    </label>

                    {isSelected && (
                      <div className="pt-2 pl-7 space-y-1">
                        <label className="block text-[11px] font-bold text-amber-900 uppercase tracking-wider">
                          Why are you challenging Question {idx + 1}? *
                        </label>
                        <textarea
                          rows={2}
                          required
                          value={challengeReasons[q.questionId] || ""}
                          onChange={(e) =>
                            setChallengeReasons((prev) => ({
                              ...prev,
                              [q.questionId]: e.target.value
                            }))
                          }
                          placeholder="e.g. In Step 2, I defined rate of change of momentum in words before writing the formula. Please re-check."
                          className="w-full p-2.5 text-xs border border-amber-300 rounded-xl focus:ring-2 focus:ring-amber-500 outline-none bg-white"
                        ></textarea>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="p-5 border-t border-slate-100 bg-slate-50 shrink-0 flex items-center justify-between">
              <button
                type="button"
                onClick={() => setIsChallengeModalOpen(false)}
                className="px-4 py-2 text-xs font-semibold text-slate-600 hover:text-slate-800"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={handleSubmitChallenge}
                disabled={isSubmittingDecision}
                className="px-6 py-2.5 bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs rounded-xl shadow transition flex items-center space-x-1.5"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Submit Academic Challenge to Teacher</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
