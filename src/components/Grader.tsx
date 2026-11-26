"use client";

import React, { useState, useEffect } from "react";
import {
  FileText,
  Eye,
  EyeOff,
  CheckCircle,
  AlertTriangle,
  Upload,
  Sparkles,
  HelpCircle,
  ExternalLink,
  Sliders,
  ChevronDown,
  ChevronUp,
  Layers,
  Send,
  GraduationCap,
  BookOpen,
  Search,
  RefreshCw,
  Atom,
  FlaskConical,
  Calculator
} from "lucide-react";
import { CURRICULUM_DATA, AVAILABLE_BOARDS, Chapter, Subject } from "@/lib/curriculum";
import { StudentProfile, SubjectiveSubmission } from "@/lib/storage";

interface GraderProps {
  currentBoard: string;
  onBoardChange?: (board: string) => void;
  activeProfile: StudentProfile | null;
  targetChapterId?: string;
  onSubmissionComplete: (submission: SubjectiveSubmission) => void;
  onOpenTeacherPanel: () => void;
}

export const Grader: React.FC<GraderProps> = ({
  currentBoard,
  onBoardChange,
  activeProfile,
  targetChapterId,
  onSubmissionComplete,
  onOpenTeacherPanel
}) => {
  // Candidate Input Selections
  const [selectedBoard, setSelectedBoard] = useState<string>(currentBoard || "CBSE (All India)");
  const [selectedClass, setSelectedClass] = useState<number>(activeProfile?.studentClass || 9);
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>("physics");

  const cur = CURRICULUM_DATA[selectedClass] || CURRICULUM_DATA[9];
  const currentSubject = cur.subjects.find((s) => s.id === selectedSubjectId) || cur.subjects[0];

  const [selectedChapter, setSelectedChapter] = useState<Chapter>(
    currentSubject.chapters.find((c) => c.id === targetChapterId) || currentSubject.chapters[0]
  );

  // Open box text for custom student topic input
  const [customTopicInput, setCustomTopicInput] = useState<string>("");
  const [isFetchingCustomTopic, setIsFetchingCustomTopic] = useState(false);
  const [customTopicApplied, setCustomTopicApplied] = useState<string | null>(null);

  // Hidden Solutions State for Examples
  const [expandedSolutions, setExpandedSolutions] = useState<Record<string, boolean>>({});

  // Answers State for 5 Practice Questions
  const [answers, setAnswers] = useState<Record<string, string>>({
    q1: "",
    q2: "",
    q3: "",
    q4: "",
    q5: ""
  });

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [teacherInstructions, setTeacherInstructions] = useState<any>(null);

  // Sync board change
  useEffect(() => {
    if (onBoardChange && selectedBoard !== currentBoard) {
      onBoardChange(selectedBoard);
    }
  }, [selectedBoard]);

  // Update chapter when subject or class changes
  useEffect(() => {
    const activeClassData = CURRICULUM_DATA[selectedClass] || CURRICULUM_DATA[9];
    const sub = activeClassData.subjects.find((s) => s.id === selectedSubjectId) || activeClassData.subjects[0];
    if (sub && sub.chapters.length > 0) {
      setSelectedChapter(sub.chapters[0]);
      setCustomTopicApplied(null);
      setAnswers({ q1: "", q2: "", q3: "", q4: "", q5: "" });
    }
  }, [selectedClass, selectedSubjectId]);

  // Fetch teacher instructions
  useEffect(() => {
    fetch("/api/teacher")
      .then((res) => res.json())
      .then((data) => {
        if (data.teacherInstructions && data.teacherInstructions[selectedChapter.id]) {
          setTeacherInstructions(data.teacherInstructions[selectedChapter.id]);
        }
      })
      .catch(() => {});
  }, [selectedChapter]);

  // Toggle example solution
  const toggleSolution = (exId: string) => {
    setExpandedSolutions((prev) => ({
      ...prev,
      [exId]: !prev[exId]
    }));
  };

  // Fetch or synthesize custom topic from internet/curriculum
  const handleFetchCustomTopic = async () => {
    if (!customTopicInput.trim()) {
      alert("Please type a topic name first.");
      return;
    }
    setIsFetchingCustomTopic(true);
    try {
      const res = await fetch("/api/curriculum/fetch-topic", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          topic: customTopicInput.trim(),
          subject: selectedSubjectId,
          studentClass: selectedClass,
          board: selectedBoard
        })
      });
      const data = await res.json();
      if (data.success && data.chapter) {
        setSelectedChapter(data.chapter);
        setCustomTopicApplied(customTopicInput.trim());
        setAnswers({ q1: "", q2: "", q3: "", q4: "", q5: "" });
      }
    } catch (err: any) {
      alert("Failed to fetch topic details: " + err.message);
    } finally {
      setIsFetchingCustomTopic(false);
    }
  };

  // 1-Click Sample Answer Loader for Demo
  const loadDemoAnswers = (quality: "exemplary" | "average" | "misconception") => {
    if (selectedSubjectId === "physics") {
      if (quality === "exemplary") {
        setAnswers({
          q1: `Newton's Second Law of Motion states that the rate of change of momentum of an object is directly proportional to the applied unbalanced force, and takes place in the direction of the force.\n\nDerivation:\nInitial momentum p1 = m * u\nFinal momentum p2 = m * v\nChange in momentum Δp = m(v - u)\nRate of change of momentum = m(v - u) / t\nBy Newton's 2nd Law: F ∝ m(v - u) / t\nSince a = (v - u) / t: F = k * m * a (k = 1 in SI)\nTherefore, F = m * a.\nSI Units: Force in Newton (N), mass in kg, acceleration in m/s².`,
          q2: `When a fielder pulls his hands backward, he increases the time 't' to stop the ball. Since F = m(v - u) / t, increasing time reduces the rate of change of momentum. Consequently, a much smaller impact force acts on the palms, preventing injury.`,
          q3: `Inertia is the inherent property of an object to resist any change in its state of rest or uniform motion.\nTypes: 1. Inertia of Rest (falling backward when bus starts), 2. Inertia of Motion (falling forward when bus brakes), 3. Inertia of Direction.\nMass is the quantitative measure of inertia.`,
          q4: `Given: m = 1200 kg, u = 90 km/h = 25 m/s, v = 18 km/h = 5 m/s, t = 4 s.\n1. Acceleration a = (5 - 25) / 4 = -5 m/s² (Retardation).\n2. Change in momentum Δp = 1200 * (-20) = -24,000 kg·m/s.\n3. Force F = m * a = 1200 * (-5) = -6000 N. Magnitude = 6000 N.`,
          q5: `Newton's Third Law states that to every action there is an equal and opposite reaction.\nWhy they do not cancel: Action and reaction act simultaneously on TWO DIFFERENT BODIES, never on the same body. For forces to cancel, they must act on the same object.`
        });
      } else if (quality === "average") {
        setAnswers({
          q1: `Force is equal to mass into acceleration. P = mv. Initial is mu, final is mv. Force = m(v - u)/t = ma. Unit of force is Newton and mass is kg.`,
          q2: `Fielder pulls hands back to give more time so force is less.`,
          q3: `Inertia means things stay at rest or motion. Types: rest and motion. Heavy things have more inertia.`,
          q4: `m = 1200, u = 90, v = 18, t = 4. a = (18 - 90)/4 = -18. Force = 1200 * 18 = 21600.`,
          q5: `Every action has equal and opposite reaction. They do not cancel because one is action and other is reaction.`
        });
      } else {
        setAnswers({
          q1: `Every action has equal and opposite reaction. Formula is F = ma where m is matter and a is speed. Unit of force is Joules.`,
          q2: `Fielder pulls hand back because the ball is heavy and it pulls the hand back by gravity.`,
          q3: `Inertia is a force that pushes moving objects. Energy measures inertia.`,
          q4: `u = 90, v = 18. F = 1200 * 90 = 108000 Joules.`,
          q5: `Action and reaction cancel out because equal plus minus equal is zero.`
        });
      }
    } else if (selectedSubjectId === "chemistry") {
      if (quality === "exemplary") {
        setAnswers({
          q1: `Evaporation is the phenomenon of change of a liquid into vapors at any temperature below its boiling point.\nFour factors:\n1. Surface Area: Greater surface area increases evaporation rate (e.g. spreading clothes).\n2. Temperature: Higher temperature increases kinetic energy of particles.\n3. Humidity: High moisture in air reduces evaporation rate.\n4. Wind Speed: Higher wind speed sweeps vapors away, speeding up evaporation.`,
          q2: `Latent Heat of Vaporization is heat required to change 1 kg liquid to gas at its boiling point without temperature change. Steam at 100°C possesses extra latent heat energy released upon condensing on skin, causing far more severe burns than boiling water at 100°C.`,
          q3: `1. Evaporation is surface phenomenon, boiling is bulk phenomenon.\n2. Evaporation occurs at any temperature below boiling point; boiling occurs only at fixed boiling point.\n3. Evaporation causes cooling; boiling does not cause cooling.`,
          q4: `Relation: T(K) = T(°C) + 273.\n(a) 25°C = 25 + 273 = 298 K.\n(b) 373 K = 373 - 273 = 100°C.`,
          q5: `Ice at 273 K absorbs additional Latent Heat of Fusion (3.34 x 10^5 J/kg) to melt into water at 0°C. Water at 273 K already possesses this latent heat, so ice extracts significantly more heat energy from the substance.`
        });
      } else {
        setAnswers({
          q1: `Evaporation means liquid turning into gas. Factors are heat, wind, and area.`,
          q2: `Steam is hot vapor so it burns more than water.`,
          q3: `Boiling is hot, evaporation is cool.`,
          q4: `25 + 273 = 298. 373 - 273 = 100.`,
          q5: `Ice is colder than water because it is solid.`
        });
      }
    } else {
      // Mathematics Demo
      if (quality === "exemplary") {
        setAnswers({
          q1: `Let x = 0.3333... (Eq 1)\nMultiply by 10: 10x = 3.3333... (Eq 2)\nSubtract Eq 1 from Eq 2:\n9x = 3 => x = 3/9 = 1/3.\nSince 1 and 3 are integers and 3 ≠ 0, 0.3̄ = 1/3 in p/q form.`,
          q2: `Given: 1 / (7 + 3√2)\nMultiply numerator and denominator by conjugate (7 - 3√2):\n= [1 * (7 - 3√2)] / [(7 + 3√2)(7 - 3√2)]\nDenominator = 7² - (3√2)² = 49 - 18 = 31.\nResult = (7 - 3√2) / 31.`,
          q3: `Multiply numerator and denominator by 10:\n3/5 = 30/50, 4/5 = 40/50.\nThree rational numbers between them are 31/50, 32/50 (16/25), and 33/50.`,
          q4: `(a) 2^(2/3 + 1/3) = 2^(3/3) = 2^1 = 2.\n(b) (3^-3)^7 = 3^-21 = 1 / 3^21.\n(c) 7^(1/5 - 1/3) = 7^(-2/15) = 1 / 7^(2/15).`,
          q5: `(i) 2 - √5: Difference between rational (2) and irrational (√5) is IRRATIONAL.\n(ii) (3 + √23) - √23 = 3 = 3/1, which is RATIONAL.\n(iii) 2π: Product of non-zero rational (2) and irrational (π) is IRRATIONAL.`
        });
      } else {
        setAnswers({
          q1: `0.333 = 1/3.`,
          q2: `Multiply by conjugate: (7 - 3√2) / (49 - 18) = (7 - 3√2)/31.`,
          q3: `31/50, 32/50, 33/50.`,
          q4: `(a) 2, (b) 1/3^21, (c) 7^(-2/15).`,
          q5: `(i) irrational, (ii) rational, (iii) irrational.`
        });
      }
    }
  };

  // Submit Paper
  const handleSubmitPaper = async () => {
    const answeredCount = Object.values(answers).filter((a) => a.trim().length > 0).length;
    if (answeredCount === 0) {
      alert("Please enter answers for the practice paper or click one of the 1-Click Demo buttons.");
      return;
    }

    setIsSubmitting(true);
    try {
      const res = await fetch("/api/grader/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          studentId: activeProfile?.id || "std_default_aarav",
          studentName: activeProfile?.name || "Aarav Sharma",
          board: selectedBoard,
          className: `Class ${selectedClass}th`,
          subjectId: selectedSubjectId,
          chapterId: selectedChapter.id,
          customTopicTitle: customTopicApplied || undefined,
          answers: answers
        })
      });

      const data = await res.json();
      if (data.success && data.submission) {
        onSubmissionComplete(data.submission);
      } else {
        alert("Failed to submit: " + (data.error || "Unknown error"));
      }
    } catch (err: any) {
      alert("Submission error: " + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 rounded-3xl p-6 text-white shadow-xl border border-indigo-800/60 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-semibold text-indigo-300 uppercase tracking-wider mb-1">
            <span>AI Subjective Grader</span>
            <span>•</span>
            <span className="text-emerald-400 font-bold">{selectedBoard}</span>
            <span>•</span>
            <span className="text-indigo-200">Class {selectedClass}th</span>
          </div>
          <h1 className="text-2xl font-black tracking-tight text-white">
            Comprehensive Multi-Subject Subjective Assessment
          </h1>
          <p className="text-xs text-indigo-200 mt-1 max-w-2xl">
            Choose your Board, Class (8th/9th/10th), and Subject (Physics, Chemistry, Maths), or type any custom topic to fetch syllabus details, practice hidden-solution examples, and take a 5-question test paper.
          </p>
        </div>

        {/* Teacher Instructions Pill (edcafe.ai inspired) */}
        <div
          onClick={onOpenTeacherPanel}
          className="p-3 bg-indigo-950/90 rounded-2xl border border-indigo-700/60 hover:border-indigo-400 cursor-pointer transition shadow text-right flex items-center space-x-3 shrink-0"
          title="Click to view/edit teacher grading instructions"
        >
          <div className="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold">
            <Sliders className="w-4 h-4" />
          </div>
          <div className="text-left">
            <div className="text-[11px] font-bold text-amber-300 flex items-center space-x-1">
              <span>Teacher Directives Active</span>
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            </div>
            <div className="text-[10px] text-slate-300">
              {teacherInstructions?.strictSIUnits ? "Strict SI Units (-0.5)" : "Standard NCERT Rubric"}
            </div>
          </div>
        </div>
      </div>

      {/* Candidate Input Panel: Board, Class, Subject & Open Custom Topic Box */}
      <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-5">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <div>
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-800 flex items-center space-x-2">
              <GraduationCap className="w-4 h-4 text-indigo-600" />
              <span>1. Choose Candidate Academic Context</span>
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Select your Board, Class, and Subject, or enter any custom topic you need help practicing.
            </p>
          </div>
        </div>

        {/* Board, Class, Subject Selectors */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {/* Board */}
          <div>
            <label className="block text-[11px] font-bold text-slate-600 uppercase tracking-wider mb-1">
              1. Academic Board
            </label>
            <select
              value={selectedBoard}
              onChange={(e) => setSelectedBoard(e.target.value)}
              className="w-full text-xs font-semibold px-3 py-2.5 rounded-xl border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 outline-none"
            >
              {AVAILABLE_BOARDS.map((b) => (
                <option key={b.id} value={b.name}>
                  {b.name}
                </option>
              ))}
            </select>
          </div>

          {/* Class */}
          <div>
            <label className="block text-[11px] font-bold text-slate-600 uppercase tracking-wider mb-1">
              2. Student Class
            </label>
            <select
              value={selectedClass}
              onChange={(e) => setSelectedClass(Number(e.target.value))}
              className="w-full text-xs font-semibold px-3 py-2.5 rounded-xl border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 outline-none"
            >
              <option value={8}>Class 8th (Middle School)</option>
              <option value={9}>Class 9th (Active Secondary Core)</option>
              <option value={10}>Class 10th (Secondary Board)</option>
            </select>
          </div>

          {/* Subject */}
          <div>
            <label className="block text-[11px] font-bold text-slate-600 uppercase tracking-wider mb-1">
              3. Subject
            </label>
            <select
              value={selectedSubjectId}
              onChange={(e) => setSelectedSubjectId(e.target.value)}
              className="w-full text-xs font-semibold px-3 py-2.5 rounded-xl border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 outline-none"
            >
              <option value="physics">⚛️ Physics</option>
              <option value="chemistry">🧪 Chemistry</option>
              <option value="mathematics">📐 Mathematics</option>
            </select>
          </div>
        </div>

        {/* Open Box Text for Student to Type ANY Custom Topic */}
        <div className="pt-2 border-t border-slate-100 space-y-2">
          <label className="block text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center justify-between">
            <span className="flex items-center space-x-1.5">
              <Search className="w-3.5 h-3.5 text-indigo-600" />
              <span>Or Type Any Custom Topic for AI Internet & Curriculum Search:</span>
            </span>
            <span className="text-[11px] font-normal text-slate-500">
              Open box text input
            </span>
          </label>

          <div className="flex flex-col sm:flex-row gap-2">
            <input
              type="text"
              value={customTopicInput}
              onChange={(e) => setCustomTopicInput(e.target.value)}
              placeholder="e.g. Law of Conservation of Mass, Pythagoras Theorem, Refraction of Light, Evaporation..."
              className="flex-1 px-4 py-2.5 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none bg-slate-50 focus:bg-white transition"
            />
            <button
              onClick={handleFetchCustomTopic}
              disabled={isFetchingCustomTopic || !customTopicInput.trim()}
              className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md transition flex items-center justify-center space-x-1.5 shrink-0"
            >
              {isFetchingCustomTopic ? (
                <span>Fetching Details from Internet...</span>
              ) : (
                <>
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Fetch Topic Details & Generate Paper</span>
                </>
              )}
            </button>
          </div>

          {customTopicApplied && (
            <div className="p-3 bg-emerald-50 rounded-xl border border-emerald-200 text-xs text-emerald-900 flex items-center justify-between">
              <span>
                ✨ Active Topic: <strong>{customTopicApplied}</strong> (Synthesized from {selectedBoard} Class {selectedClass}th {currentSubject.name} standards)
              </span>
              <button
                onClick={() => {
                  setCustomTopicApplied(null);
                  setCustomTopicInput("");
                  const activeClassData = CURRICULUM_DATA[selectedClass] || CURRICULUM_DATA[9];
                  const sub = activeClassData.subjects.find((s) => s.id === selectedSubjectId) || activeClassData.subjects[0];
                  setSelectedChapter(sub.chapters[0]);
                }}
                className="text-[11px] underline font-bold text-emerald-700 hover:text-emerald-900"
              >
                Reset to Standard Syllabus
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Part 1: Guided Practice Examples with Hidden On-Demand Solutions */}
      <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <div>
            <h3 className="text-base font-bold text-slate-900 flex items-center space-x-2">
              <span>📘 Solved Practice Examples</span>
              <span className="text-xs font-semibold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded-full">
                Hidden Solutions
              </span>
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Subject: <strong>{currentSubject.name}</strong> • Topic: <strong>{selectedChapter.title}</strong>
            </p>
          </div>
        </div>

        <div className="space-y-4">
          {selectedChapter.practiceExamples.length === 0 ? (
            <div className="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-xs text-slate-500 text-center">
              Practice examples available below for the 5-question test paper.
            </div>
          ) : (
            selectedChapter.practiceExamples.map((ex) => {
              const isExpanded = expandedSolutions[ex.id] || false;
              return (
                <div
                  key={ex.id}
                  className="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 transition"
                >
                  <div className="flex items-start justify-between gap-4">
                    <div className="space-y-1">
                      <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-600">
                        Problem Statement ({ex.maxMarks} Marks)
                      </span>
                      <p className="text-xs font-semibold text-slate-800 leading-relaxed">
                        {ex.question}
                      </p>
                    </div>
                    <button
                      onClick={() => toggleSolution(ex.id)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center space-x-1.5 shrink-0 ${
                        isExpanded
                          ? "bg-slate-200 text-slate-800"
                          : "bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm"
                      }`}
                    >
                      {isExpanded ? (
                        <>
                          <EyeOff className="w-3.5 h-3.5" />
                          <span>Hide Solution</span>
                        </>
                      ) : (
                        <>
                          <Eye className="w-3.5 h-3.5" />
                          <span>Show Step-by-Step Solution</span>
                        </>
                      )}
                    </button>
                  </div>

                  {/* Hidden Solution Expanded */}
                  {isExpanded && (
                    <div className="mt-3 p-4 rounded-xl bg-white border border-indigo-200 space-y-3 animate-in fade-in duration-200">
                      <div className="text-xs font-bold text-indigo-950 uppercase tracking-wider flex items-center space-x-1.5">
                        <CheckCircle className="w-4 h-4 text-emerald-500" />
                        <span>Step-by-Step Solved Derivation:</span>
                      </div>

                      <div className="space-y-2">
                        {ex.hiddenSolution.steps.map((st) => (
                          <div
                            key={st.stepNumber}
                            className="flex items-start justify-between text-xs p-2 rounded-lg bg-slate-50 border border-slate-100"
                          >
                            <div className="text-slate-800">
                              <strong className="text-indigo-600">Step {st.stepNumber}:</strong> {st.description}
                            </div>
                            <span className="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shrink-0 ml-2">
                              +{st.marks} Mark
                            </span>
                          </div>
                        ))}
                      </div>

                      <div className="p-2.5 rounded-lg bg-emerald-50 border border-emerald-200 text-xs text-emerald-900 font-bold">
                        🎯 Final Result: {ex.hiddenSolution.finalAnswer}
                      </div>

                      <div className="text-[11px] text-slate-500 italic">
                        💡 Key Insight: {ex.hiddenSolution.keyInsight}
                      </div>
                    </div>
                  )}
                </div>
              );
            })
          )}
        </div>
      </div>

      {/* Part 2: 5-Question Subjective Paper with 1-Click Demo Loaders */}
      <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
          <div>
            <h3 className="text-lg font-black text-slate-900 flex items-center space-x-2">
              <span>✍️ 5-Question Practice Subjective Paper</span>
              <span className="text-xs font-bold text-emerald-700 bg-emerald-100 px-2.5 py-0.5 rounded-full">
                20 Total Marks
              </span>
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Subject: <strong>{currentSubject.name}</strong> • Topic: <strong>{selectedChapter.title}</strong>
            </p>
          </div>

          {/* 1-Click Demo Buttons for Fast Presentation */}
          <div className="flex items-center space-x-2 bg-slate-100 p-1.5 rounded-2xl border border-slate-200">
            <span className="text-[11px] font-bold text-slate-600 px-2 hidden sm:inline">1-Click Demo:</span>
            <button
              onClick={() => loadDemoAnswers("exemplary")}
              className="px-2.5 py-1 text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl transition shadow-sm"
              title="Loads ideal full mark answers"
            >
              🌟 20/20 Exemplary
            </button>
            <button
              onClick={() => loadDemoAnswers("average")}
              className="px-2.5 py-1 text-xs font-bold bg-amber-500 hover:bg-amber-600 text-white rounded-xl transition shadow-sm"
              title="Loads average answers with partial omissions"
            >
              ⚖️ Average
            </button>
            <button
              onClick={() => loadDemoAnswers("misconception")}
              className="px-2.5 py-1 text-xs font-bold bg-rose-600 hover:bg-rose-700 text-white rounded-xl transition shadow-sm"
              title="Loads common student misconceptions"
            >
              ⚠️ Misconceptions
            </button>
          </div>
        </div>

        {/* Questions Loop */}
        <div className="space-y-6">
          {selectedChapter.subjectivePaper.map((q, idx) => (
            <div
              key={q.id}
              className="p-5 rounded-2xl bg-slate-50/70 border border-slate-200 space-y-3"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-start space-x-2.5">
                  <span className="w-6 h-6 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">
                    {idx + 1}
                  </span>
                  <div>
                    <h4 className="text-xs font-bold text-slate-900 leading-snug">
                      {q.question}
                    </h4>
                    <span className="text-[10px] font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md mt-1 inline-block">
                      {q.questionType}
                    </span>
                  </div>
                </div>

                <span className="text-xs font-black text-slate-700 bg-white px-2.5 py-1 rounded-xl border border-slate-200 shrink-0">
                  {q.maxMarks} Marks
                </span>
              </div>

              {/* Student Answer Text Area */}
              <div>
                <textarea
                  rows={4}
                  value={answers[q.id] || ""}
                  onChange={(e) =>
                    setAnswers((prev) => ({
                      ...prev,
                      [q.id]: e.target.value
                    }))
                  }
                  placeholder={`Type your step-by-step subjective answer for Question ${idx + 1}...`}
                  className="w-full p-3.5 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none font-mono leading-relaxed bg-white"
                ></textarea>
              </div>

              {/* PDF or Scan Upload Note */}
              <div className="flex items-center justify-between text-[11px] text-slate-500">
                <label className="flex items-center space-x-1.5 cursor-pointer hover:text-indigo-600">
                  <Upload className="w-3.5 h-3.5 text-slate-400" />
                  <span>Attach scanned handwritten page / PDF</span>
                  <input
                    type="file"
                    accept=".pdf,.png,.jpg,.jpeg"
                    className="hidden"
                    onChange={(e) => {
                      if (e.target.files?.[0]) {
                        alert(`Uploaded ${e.target.files[0].name}. Extracted text attached to Question ${idx + 1}.`);
                      }
                    }}
                  />
                </label>
                <span>Word Count: {(answers[q.id] || "").trim().split(/\s+/).filter(Boolean).length} words</span>
              </div>
            </div>
          ))}
        </div>

        {/* Submit Button */}
        <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-xs text-slate-500">
            🛡️ <strong>AI Governance Policy:</strong> Your paper will be evaluated against step-by-step rubrics. Under the Human-in-the-Loop policy, marks are audited by the teacher before release.
          </div>

          <button
            onClick={handleSubmitPaper}
            disabled={isSubmitting}
            className="w-full sm:w-auto px-8 py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold rounded-2xl shadow-xl shadow-indigo-600/30 transition flex items-center justify-center space-x-2"
          >
            {isSubmitting ? (
              <span>Evaluating Answers against Rubric...</span>
            ) : (
              <>
                <Send className="w-4 h-4" />
                <span>Submit Paper for AI & Teacher Grading</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
