"use client";

import React, { useState, useEffect } from "react";
import {
  ShieldCheck,
  CheckCircle,
  Clock,
  AlertTriangle,
  Sliders,
  Edit3,
  Save,
  Send,
  Eye,
  MessageSquare,
  Sparkles,
  RefreshCw
} from "lucide-react";
import { SubjectiveSubmission, TeacherInstruction } from "@/lib/storage";

interface TeacherPanelProps {
  onSelectSubmissionToReview: (sub: SubjectiveSubmission) => void;
}

export const TeacherPanel: React.FC<TeacherPanelProps> = ({ onSelectSubmissionToReview }) => {
  const [submissions, setSubmissions] = useState<SubjectiveSubmission[]>([]);
  const [teacherInstructions, setTeacherInstructions] = useState<Record<string, TeacherInstruction>>({});
  const [loading, setLoading] = useState(true);

  // Active review submission
  const [selectedSub, setSelectedSub] = useState<SubjectiveSubmission | null>(null);
  const [teacherFeedback, setTeacherFeedback] = useState("");
  const [editingMarks, setEditingMarks] = useState<Record<string, number>>({});
  const [resolutionNotes, setResolutionNotes] = useState<Record<string, string>>({});

  // Teacher Rubric Configuration tab (like edcafe.ai)
  const [activeTab, setActiveTab] = useState<"audit_queue" | "edcafe_rubrics">("audit_queue");
  const [rubricText, setRubricText] = useState(
    "Focus strictly on proper statement of Newton's 2nd Law (rate of change of momentum). Penalize 0.5 marks if SI units (N, kg, m/s²) are omitted. Allow partial marks for mathematical derivation steps."
  );
  const [strictSI, setStrictSI] = useState(true);
  const [partialSteps, setPartialSteps] = useState(true);
  const [lenientSpell, setLenientSpell] = useState(true);

  const fetchSubmissions = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/teacher");
      const data = await res.json();
      setSubmissions(data.submissions || []);
      setTeacherInstructions(data.teacherInstructions || {});
      if (data.submissions && data.submissions.length > 0 && !selectedSub) {
        setSelectedSub(data.submissions[0]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSubmissions();
  }, []);

  useEffect(() => {
    if (selectedSub) {
      const initialMarks: Record<string, number> = {};
      selectedSub.questions.forEach((q) => {
        initialMarks[q.questionId] = q.teacherOverrideMarks ?? q.awardedMarks;
      });
      setEditingMarks(initialMarks);
      setTeacherFeedback(selectedSub.teacherOverallFeedback || "");
    }
  }, [selectedSub]);

  // Release Marks to Student
  const handleReleaseMarks = async () => {
    if (!selectedSub) return;
    try {
      const res = await fetch("/api/teacher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "RELEASE_MARKS",
          submissionId: selectedSub.id,
          teacherFeedback: teacherFeedback
        })
      });
      const data = await res.json();
      if (data.success) {
        alert("Success! Marks have been officially released to the student.");
        fetchSubmissions();
        setSelectedSub(data.submission);
      }
    } catch (err: any) {
      alert("Error: " + err.message);
    }
  };

  // Save single question score override
  const handleUpdateScore = async (qId: string) => {
    if (!selectedSub) return;
    const newScore = editingMarks[qId];
    try {
      const res = await fetch("/api/teacher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "UPDATE_MARKS",
          submissionId: selectedSub.id,
          questionId: qId,
          newMarks: newScore
        })
      });
      const data = await res.json();
      if (data.success) {
        setSelectedSub(data.submission);
        fetchSubmissions();
      }
    } catch (err: any) {
      alert("Error updating marks: " + err.message);
    }
  };

  // Resolve Student Challenge
  const handleResolveChallenge = async (qId: string) => {
    if (!selectedSub) return;
    const newScore = editingMarks[qId];
    const notes = resolutionNotes[qId] || "Reviewed by Senior Physics Faculty. Marks updated accordingly.";
    try {
      const res = await fetch("/api/teacher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "RESOLVE_CHALLENGE",
          submissionId: selectedSub.id,
          questionId: qId,
          newMarks: newScore,
          resolutionNotes: notes
        })
      });
      const data = await res.json();
      if (data.success) {
        alert("Challenge resolved and updated marks re-released to student.");
        setSelectedSub(data.submission);
        fetchSubmissions();
      }
    } catch (err: any) {
      alert("Error resolving challenge: " + err.message);
    }
  };

  // Save EdCafe-style rubric instructions
  const handleSaveRubricInstructions = async () => {
    try {
      const res = await fetch("/api/teacher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "SAVE_INSTRUCTIONS",
          instructionData: {
            topicId: "force_and_laws",
            specificInstructions: rubricText,
            strictSIUnits: strictSI,
            partialCreditForSteps: partialSteps,
            lenientSpelling: lenientSpell
          }
        })
      });
      const data = await res.json();
      if (data.success) {
        alert("Custom Teacher Instructions saved! Future AI evaluations will strictly follow these directives.");
      }
    } catch (err: any) {
      alert("Error saving instructions: " + err.message);
    }
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Teacher Header Banner */}
      <div className="bg-gradient-to-r from-amber-950 via-slate-900 to-amber-950 rounded-3xl p-6 text-white shadow-xl border border-amber-800/60 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-semibold text-amber-300 uppercase tracking-wider mb-1">
            <Sliders className="w-3.5 h-3.5 text-amber-400" />
            <span>Teacher & Governance Audit Console</span>
          </div>
          <h1 className="text-2xl font-black tracking-tight text-white">
            Human-in-the-Loop Evaluation & Controlled Release
          </h1>
          <p className="text-xs text-amber-200 mt-1 max-w-2xl">
            Configure custom rubric directives (like www.edcafe.ai), audit AI step-by-step scoring, override marks, release final scores to students, and adjudicate academic appeals.
          </p>
        </div>

        {/* Tab Switcher */}
        <div className="flex space-x-1.5 bg-slate-950/80 p-1.5 rounded-2xl border border-amber-700/50">
          <button
            onClick={() => setActiveTab("audit_queue")}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition ${
              activeTab === "audit_queue" ? "bg-amber-600 text-white shadow" : "text-slate-400 hover:text-white"
            }`}
          >
            Audit & Release Queue ({submissions.length})
          </button>
          <button
            onClick={() => setActiveTab("edcafe_rubrics")}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition ${
              activeTab === "edcafe_rubrics" ? "bg-amber-600 text-white shadow" : "text-slate-400 hover:text-white"
            }`}
          >
            Teacher Directives (EdCafe Style)
          </button>
        </div>
      </div>

      {activeTab === "edcafe_rubrics" ? (
        /* Teacher Rubric Directives Tab */
        <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-5">
          <div>
            <h3 className="text-base font-bold text-slate-900">
              Teacher Instructions Configuration (Inspired by www.edcafe.ai)
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Specify your exact grading preferences, penalty rules, and step-weight allocations. EduAegis enforces these instructions during AI evaluation.
            </p>
          </div>

          <div className="space-y-4">
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                Custom Teacher Directives for "Force & Laws of Motion"
              </label>
              <textarea
                rows={4}
                value={rubricText}
                onChange={(e) => setRubricText(e.target.value)}
                className="w-full p-3.5 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-amber-500 outline-none leading-relaxed"
                placeholder="Type specific guidelines for grading student answers..."
              ></textarea>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              <label className="p-3.5 rounded-2xl border border-slate-200 bg-slate-50 flex items-center space-x-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={strictSI}
                  onChange={(e) => setStrictSI(e.target.checked)}
                  className="w-4 h-4 text-amber-600 rounded focus:ring-amber-500"
                />
                <div>
                  <div className="text-xs font-bold text-slate-900">Strict SI Units Check</div>
                  <div className="text-[10px] text-slate-500">Penalize -0.5 if N, kg, m/s² are missing</div>
                </div>
              </label>

              <label className="p-3.5 rounded-2xl border border-slate-200 bg-slate-50 flex items-center space-x-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={partialSteps}
                  onChange={(e) => setPartialSteps(e.target.checked)}
                  className="w-4 h-4 text-amber-600 rounded focus:ring-amber-500"
                />
                <div>
                  <div className="text-xs font-bold text-slate-900">Partial Step Credit</div>
                  <div className="text-[10px] text-slate-500">Award marks for correct formulas even if calculation has minor error</div>
                </div>
              </label>

              <label className="p-3.5 rounded-2xl border border-slate-200 bg-slate-50 flex items-center space-x-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={lenientSpell}
                  onChange={(e) => setLenientSpell(e.target.checked)}
                  className="w-4 h-4 text-amber-600 rounded focus:ring-amber-500"
                />
                <div>
                  <div className="text-xs font-bold text-slate-900">Lenient Spelling</div>
                  <div className="text-[10px] text-slate-500">Do not penalize grammar if physics meaning is accurate</div>
                </div>
              </label>
            </div>

            <button
              onClick={handleSaveRubricInstructions}
              className="px-6 py-2.5 bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs rounded-xl shadow transition flex items-center space-x-2"
            >
              <Save className="w-3.5 h-3.5" />
              <span>Save & Apply Teacher Directives</span>
            </button>
          </div>
        </div>
      ) : (
        /* Audit & Release Queue */
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Submissions List */}
          <div className="lg:col-span-4 space-y-3">
            <div className="flex items-center justify-between text-xs font-bold uppercase tracking-wider text-slate-500 px-1">
              <span>Submissions ({submissions.length})</span>
              <button
                onClick={fetchSubmissions}
                className="hover:text-amber-600 flex items-center space-x-1"
              >
                <RefreshCw className="w-3 h-3" />
                <span>Refresh</span>
              </button>
            </div>

            {submissions.length === 0 ? (
              <div className="p-8 bg-white rounded-3xl border border-slate-200 text-center text-xs text-slate-500">
                No submissions recorded yet. Go to the AI Grader to submit a practice test!
              </div>
            ) : (
              <div className="space-y-2">
                {submissions.map((sub) => {
                  const isPending = sub.status === "PENDING_TEACHER_RELEASE";
                  const isChallenged = sub.status === "CHALLENGED";
                  const isReleased = sub.status === "RELEASED";
                  const isAccepted = sub.status === "ACCEPTED";

                  return (
                    <div
                      key={sub.id}
                      onClick={() => setSelectedSub(sub)}
                      className={`p-4 rounded-2xl border transition cursor-pointer space-y-1.5 ${
                        selectedSub?.id === sub.id
                          ? "bg-amber-50/80 border-amber-400 shadow-sm"
                          : "bg-white hover:bg-slate-50 border-slate-200"
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-xs font-bold text-slate-900">{sub.studentName}</span>
                        <span className="text-xs font-black text-indigo-600">
                          {sub.totalAwardedMarks} / {sub.totalMaxMarks}
                        </span>
                      </div>

                      <div className="text-[11px] text-slate-500">
                        {sub.chapterTitle} • {sub.board}
                      </div>

                      <div className="pt-1 flex items-center justify-between text-[10px]">
                        {isPending && (
                          <span className="font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded-full flex items-center space-x-1">
                            <Clock className="w-3 h-3" />
                            <span>Needs Audit</span>
                          </span>
                        )}
                        {isChallenged && (
                          <span className="font-bold text-rose-700 bg-rose-100 px-2 py-0.5 rounded-full flex items-center space-x-1">
                            <AlertTriangle className="w-3 h-3" />
                            <span>Student Challenged!</span>
                          </span>
                        )}
                        {isReleased && (
                          <span className="font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">
                            Released
                          </span>
                        )}
                        {isAccepted && (
                          <span className="font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded-full">
                            Accepted by Student
                          </span>
                        )}
                        <span className="text-slate-400">
                          {new Date(sub.submittedAt).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>

          {/* Active Audit Pane */}
          <div className="lg:col-span-8 space-y-5">
            {selectedSub ? (
              <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
                {/* Header */}
                <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
                  <div>
                    <span className="text-xs font-bold text-amber-700 uppercase tracking-wider">
                      Audit Workspace
                    </span>
                    <h3 className="text-lg font-black text-slate-900 mt-0.5">
                      Reviewing: {selectedSub.studentName}'s Answer Sheet
                    </h3>
                    <p className="text-xs text-slate-500">
                      {selectedSub.chapterTitle} • Total Marks: <strong>{selectedSub.totalAwardedMarks} / {selectedSub.totalMaxMarks}</strong>
                    </p>
                  </div>

                  {/* Release Marks Button */}
                  {selectedSub.status === "PENDING_TEACHER_RELEASE" && (
                    <button
                      onClick={handleReleaseMarks}
                      className="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs rounded-xl shadow-lg shadow-emerald-600/30 transition flex items-center space-x-1.5"
                    >
                      <CheckCircle className="w-4 h-4" />
                      <span>Release Marks to Student</span>
                    </button>
                  )}
                </div>

                {/* Teacher Overall Remarks input */}
                <div className="p-4 bg-slate-50 rounded-2xl border border-slate-200 space-y-2">
                  <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                    Teacher Overall Feedback to Student:
                  </label>
                  <div className="flex space-x-2">
                    <input
                      type="text"
                      value={teacherFeedback}
                      onChange={(e) => setTeacherFeedback(e.target.value)}
                      placeholder="e.g. Well articulated derivation in Q1. Be careful with unit conversions in Q4."
                      className="flex-1 px-3 py-2 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-amber-500 outline-none"
                    />
                    <button
                      onClick={handleReleaseMarks}
                      className="px-3 py-2 bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold rounded-xl"
                    >
                      Save Remarks
                    </button>
                  </div>
                </div>

                {/* Questions Audit List */}
                <div className="space-y-4">
                  <div className="text-xs font-bold uppercase tracking-wider text-slate-500">
                    Question-by-Question Evaluation & Mark Override:
                  </div>

                  {selectedSub.questions.map((q, idx) => (
                    <div
                      key={q.questionId}
                      className={`p-5 rounded-2xl border transition space-y-3 ${
                        q.isChallenged
                          ? "bg-rose-50/70 border-rose-300 ring-2 ring-rose-400/20"
                          : "bg-slate-50/70 border-slate-200"
                      }`}
                    >
                      <div className="flex items-start justify-between gap-3">
                        <div>
                          <div className="flex items-center space-x-2">
                            <span className="text-[11px] font-bold text-indigo-700">Question {idx + 1}</span>
                            {q.isChallenged && (
                              <span className="text-[10px] font-bold bg-rose-600 text-white px-2 py-0.5 rounded-full">
                                Student Challenged!
                              </span>
                            )}
                          </div>
                          <h4 className="text-xs font-bold text-slate-900 mt-0.5">{q.questionText}</h4>
                        </div>

                        {/* Teacher Mark Override Input */}
                        <div className="flex items-center space-x-1.5 shrink-0 bg-white p-1 rounded-xl border border-slate-200">
                          <span className="text-[11px] font-semibold text-slate-500 pl-1.5">Marks:</span>
                          <input
                            type="number"
                            step="0.5"
                            min="0"
                            max={q.maxMarks}
                            value={editingMarks[q.questionId] ?? q.awardedMarks}
                            onChange={(e) =>
                              setEditingMarks((prev) => ({
                                ...prev,
                                [q.questionId]: Number(e.target.value)
                              }))
                            }
                            className="w-14 px-2 py-1 text-xs font-bold border border-slate-300 rounded-lg text-center"
                          />
                          <span className="text-[11px] text-slate-400 pr-1">/ {q.maxMarks}</span>
                          <button
                            onClick={() => handleUpdateScore(q.questionId)}
                            className="p-1 hover:bg-slate-100 rounded text-indigo-600 font-bold"
                            title="Save Override"
                          >
                            <Save className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </div>

                      {/* Student's Answer */}
                      <div className="text-[11px] font-mono text-slate-700 bg-white p-2.5 rounded-xl border border-slate-200 whitespace-pre-wrap">
                        {q.studentAnswer}
                      </div>

                      {/* AI Step Breakdown */}
                      <div className="space-y-1">
                        <span className="text-[10px] font-bold text-slate-500 uppercase">AI Step Rubric:</span>
                        {q.stepBreakdown.map((s) => (
                          <div key={s.stepNumber} className="text-[11px] text-slate-600 flex justify-between bg-white/70 p-1.5 rounded-lg border border-slate-200">
                            <span>Step {s.stepNumber} ({s.stepFocus}): {s.whyAwardedOrDeducted}</span>
                            <strong className="text-slate-800 ml-2">{s.marksAwarded}/{s.maxMarks}</strong>
                          </div>
                        ))}
                      </div>

                      {/* If Challenged: Adjudication Interface */}
                      {q.isChallenged && (
                        <div className="p-3 bg-white rounded-xl border border-rose-200 space-y-2">
                          <div className="text-xs font-bold text-rose-900">
                            Student Challenge Rationale:
                          </div>
                          <p className="text-xs text-slate-700 italic">
                            "{q.studentChallengeReason}"
                          </p>
                          <div className="pt-1 space-y-1.5">
                            <label className="block text-[11px] font-bold text-slate-700">
                              Teacher Appeal Resolution Remarks:
                            </label>
                            <div className="flex space-x-2">
                              <input
                                type="text"
                                placeholder="e.g. Re-checked. 0.5 marks awarded for definition step."
                                value={resolutionNotes[q.questionId] || ""}
                                onChange={(e) =>
                                  setResolutionNotes((prev) => ({
                                    ...prev,
                                    [q.questionId]: e.target.value
                                  }))
                                }
                                className="flex-1 px-2.5 py-1.5 text-xs border border-slate-300 rounded-lg outline-none"
                              />
                              <button
                                onClick={() => handleResolveChallenge(q.questionId)}
                                className="px-3 py-1.5 bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold rounded-lg"
                              >
                                Resolve & Re-Release
                              </button>
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div className="p-12 bg-white rounded-3xl border border-slate-200 text-center text-xs text-slate-500">
                Select a submission on the left to start auditing.
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
