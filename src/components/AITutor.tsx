"use client";

import React, { useState, useEffect, useRef } from "react";
import {
  BookOpen,
  Volume2,
  VolumeX,
  Play,
  Pause,
  RotateCcw,
  Sparkles,
  Video,
  Upload,
  ArrowRight,
  CheckCircle,
  AlertCircle,
  ExternalLink,
  ChevronRight,
  Layers,
  HelpCircle,
  FileText,
  Search,
  GraduationCap,
  Atom,
  FlaskConical,
  Calculator
} from "lucide-react";
import { CURRICULUM_DATA, AVAILABLE_BOARDS, Subject, Chapter, ConceptDetail } from "@/lib/curriculum";

interface AITutorProps {
  currentBoard: string;
  onNavigateToGrader: (chapterId: string) => void;
}

export const AITutor: React.FC<AITutorProps> = ({ currentBoard, onNavigateToGrader }) => {
  // Navigation states
  const [selectedClass, setSelectedClass] = useState<number>(9);
  const classCurriculum = CURRICULUM_DATA[selectedClass] || CURRICULUM_DATA[9];

  const [selectedSubject, setSelectedSubject] = useState<Subject>(classCurriculum.subjects[0]);
  const [selectedChapter, setSelectedChapter] = useState<Chapter>(classCurriculum.subjects[0].chapters[0]);
  const [selectedConcept, setSelectedConcept] = useState<ConceptDetail>(
    classCurriculum.subjects[0].chapters[0].concepts[0]
  );

  // Open box text for custom topic inquiry
  const [customTopicQuery, setCustomTopicQuery] = useState("");
  const [isSearchingTopic, setIsSearchingTopic] = useState(false);
  const [searchedTopicResult, setSearchedTopicResult] = useState<ConceptDetail | null>(null);

  // Teaching input modes
  const [learningMode, setLearningMode] = useState<"standard" | "custom_ingest">("standard");
  const [customInputType, setCustomInputType] = useState<"youtube" | "document">("youtube");
  const [youtubeUrl, setYoutubeUrl] = useState("https://www.youtube.com/watch?v=kKKM8Y-u7ds");
  const [documentText, setDocumentText] = useState("");
  const [ingestedLesson, setIngestedLesson] = useState<any>(null);
  const [ingesting, setIngesting] = useState(false);

  // Progressive Interactive Examples Loop
  const [revealedExamplesCount, setRevealedExamplesCount] = useState<number>(1);
  const [studentMasteryStatus, setStudentMasteryStatus] = useState<"learning" | "mastered">("learning");

  // Audio Speech Synthesis
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);
  const [speechRate, setSpeechRate] = useState<number>(1.0);
  const speechUtteranceRef = useRef<SpeechSynthesisUtterance | null>(null);

  // Update selected subject/chapter when class changes
  useEffect(() => {
    const cur = CURRICULUM_DATA[selectedClass] || CURRICULUM_DATA[9];
    if (cur.subjects.length > 0) {
      setSelectedSubject(cur.subjects[0]);
      if (cur.subjects[0].chapters.length > 0) {
        setSelectedChapter(cur.subjects[0].chapters[0]);
        if (cur.subjects[0].chapters[0].concepts.length > 0) {
          setSelectedConcept(cur.subjects[0].chapters[0].concepts[0]);
        }
      }
    }
  }, [selectedClass]);

  // Clean speech synthesis on unmount
  useEffect(() => {
    return () => {
      if (typeof window !== "undefined" && window.speechSynthesis) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  // Stop speech when concept changes
  useEffect(() => {
    if (typeof window !== "undefined" && window.speechSynthesis) {
      window.speechSynthesis.cancel();
      setIsPlayingAudio(false);
    }
    setRevealedExamplesCount(1);
    setStudentMasteryStatus("learning");
  }, [selectedConcept, searchedTopicResult, learningMode]);

  // Search custom topic from internet/curriculum
  const handleSearchTopic = async () => {
    if (!customTopicQuery.trim()) {
      alert("Please type a topic to search.");
      return;
    }
    setIsSearchingTopic(true);
    try {
      const res = await fetch("/api/curriculum/fetch-topic", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          topic: customTopicQuery.trim(),
          subject: selectedSubject.id,
          studentClass: selectedClass,
          board: currentBoard
        })
      });
      const data = await res.json();
      if (data.success && data.chapter && data.chapter.concepts.length > 0) {
        setSearchedTopicResult(data.chapter.concepts[0]);
        setSelectedConcept(data.chapter.concepts[0]);
        setSelectedChapter(data.chapter);
      }
    } catch (err: any) {
      alert("Search error: " + err.message);
    } finally {
      setIsSearchingTopic(false);
    }
  };

  // Handle Speech Synthesis
  const handleToggleAudio = () => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) {
      alert("Speech synthesis is not supported on this browser.");
      return;
    }

    if (isPlayingAudio) {
      window.speechSynthesis.cancel();
      setIsPlayingAudio(false);
      return;
    }

    const scriptToSpeak =
      learningMode === "custom_ingest" && ingestedLesson
        ? ingestedLesson.audioScript
        : (searchedTopicResult || selectedConcept).audioScript;

    const utterance = new SpeechSynthesisUtterance(scriptToSpeak);
    utterance.rate = speechRate;
    utterance.pitch = 1.0;

    const voices = window.speechSynthesis.getVoices();
    const friendlyVoice = voices.find(
      (v) => v.lang.includes("en-IN") || v.lang.includes("en-US") || v.lang.includes("en-GB")
    );
    if (friendlyVoice) {
      utterance.voice = friendlyVoice;
    }

    utterance.onend = () => {
      setIsPlayingAudio(false);
    };

    utterance.onerror = () => {
      setIsPlayingAudio(false);
    };

    speechUtteranceRef.current = utterance;
    window.speechSynthesis.speak(utterance);
    setIsPlayingAudio(true);
  };

  // Ingest custom resource
  const handleCustomIngest = async () => {
    setIngesting(true);
    try {
      const res = await fetch("/api/tutor/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          sourceType: customInputType,
          youtubeUrl: customInputType === "youtube" ? youtubeUrl : undefined,
          content: customInputType === "document" ? documentText : undefined
        })
      });
      const data = await res.json();
      if (data.lesson) {
        setIngestedLesson(data.lesson);
      }
    } catch (err: any) {
      alert("Failed to ingest resource: " + err.message);
    } finally {
      setIngesting(false);
    }
  };

  const activeConceptToDisplay = searchedTopicResult || selectedConcept;

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Top Banner */}
      <div className="bg-gradient-to-r from-indigo-900 via-blue-900 to-slate-900 rounded-3xl p-6 text-white shadow-xl border border-indigo-800/60 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-semibold text-indigo-300 uppercase tracking-wider mb-1">
            <BookOpen className="w-3.5 h-3.5 text-emerald-400" />
            <span>AI Tutor: Concept Learning & Clearing</span>
            <span>•</span>
            <span className="text-emerald-400 font-bold">{currentBoard}</span>
          </div>
          <h1 className="text-2xl font-black tracking-tight text-white">
            Socratic Concept Learning in Simple Audio & Everyday English
          </h1>
          <p className="text-xs text-indigo-200 mt-1 max-w-2xl">
            Taught in plain, engaging English with conversational audio narration, progressive real-world examples, and multi-modal document/video ingestion across Physics, Chemistry, and Mathematics.
          </p>
        </div>

        {/* Quick Class Selection (8th, 9th, 10th) */}
        <div className="flex items-center space-x-1.5 bg-slate-950/70 p-1.5 rounded-2xl border border-indigo-700/50 shrink-0">
          {[8, 9, 10].map((c) => (
            <button
              key={c}
              onClick={() => setSelectedClass(c)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center space-x-1 ${
                selectedClass === c
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/40"
                  : "text-slate-400 hover:text-white"
              }`}
            >
              <span>Class {c}th</span>
              {c === 9 && (
                <span className="text-[9px] bg-emerald-500 text-slate-950 px-1 rounded font-black">
                  Core
                </span>
              )}
            </button>
          ))}
        </div>
      </div>

      {/* Open Box Text for Student to Type ANY Concept/Topic */}
      <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-2">
        <label className="block text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center justify-between">
          <span className="flex items-center space-x-1.5">
            <Search className="w-3.5 h-3.5 text-indigo-600" />
            <span>Type any topic or doubt to explain in simple English:</span>
          </span>
          <span className="text-[11px] font-normal text-slate-500">
            Concept clearing open box text
          </span>
        </label>
        <div className="flex flex-col sm:flex-row gap-2">
          <input
            type="text"
            value={customTopicQuery}
            onChange={(e) => setCustomTopicQuery(e.target.value)}
            placeholder="e.g. Why do clouds float?, Law of Conservation of Mass, Pythagoras Theorem, Archimedes Principle..."
            className="flex-1 px-4 py-2.5 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none bg-slate-50 focus:bg-white transition"
          />
          <button
            onClick={handleSearchTopic}
            disabled={isSearchingTopic || !customTopicQuery.trim()}
            className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md transition flex items-center justify-center space-x-1.5 shrink-0"
          >
            {isSearchingTopic ? (
              <span>Synthesizing from Internet...</span>
            ) : (
              <>
                <Sparkles className="w-3.5 h-3.5" />
                <span>Explain Concept & Listen</span>
              </>
            )}
          </button>
        </div>
        {searchedTopicResult && (
          <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200 text-xs text-emerald-900 flex items-center justify-between">
            <span>
              💡 Active Concept Explanation: <strong>{searchedTopicResult.name}</strong>
            </span>
            <button
              onClick={() => {
                setSearchedTopicResult(null);
                setCustomTopicQuery("");
              }}
              className="text-[11px] underline font-bold text-emerald-700"
            >
              Reset to Standard Topics
            </button>
          </div>
        )}
      </div>

      {/* Subject Navigation Ribbon */}
      <div>
        <div className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
          Select Subject for Class {selectedClass}th:
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {classCurriculum.subjects.map((sub) => (
            <button
              key={sub.id}
              onClick={() => {
                setSelectedSubject(sub);
                setSearchedTopicResult(null);
                if (sub.chapters.length > 0) {
                  setSelectedChapter(sub.chapters[0]);
                  if (sub.chapters[0].concepts.length > 0) {
                    setSelectedConcept(sub.chapters[0].concepts[0]);
                  }
                }
              }}
              className={`p-4 rounded-2xl border text-left transition flex items-center space-x-3.5 ${
                selectedSubject.id === sub.id
                  ? "bg-white border-indigo-600 shadow-md ring-2 ring-indigo-500/20"
                  : "bg-white/80 hover:bg-white border-slate-200"
              }`}
            >
              <div
                className={`w-10 h-10 rounded-xl bg-gradient-to-tr ${sub.accentColor} text-white flex items-center justify-center font-bold shadow`}
              >
                {sub.id === "physics" || sub.id === "physics_8" || sub.id === "physics_10" ? (
                  <Atom className="w-5 h-5" />
                ) : sub.id.includes("chem") ? (
                  <FlaskConical className="w-5 h-5" />
                ) : (
                  <Calculator className="w-5 h-5" />
                )}
              </div>
              <div>
                <div className="text-sm font-bold text-slate-900">{sub.name}</div>
                <div className="text-[11px] text-slate-500 font-medium">
                  {sub.chapters.length} Chapter{sub.chapters.length !== 1 ? "s" : ""}
                </div>
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Main Grid: Left Column = Chapters & Concepts, Right Column = Interactive Teaching Pane */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Chapters and Concepts */}
        <div className="lg:col-span-4 space-y-4">
          {/* Chapter Selector */}
          <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-3">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center justify-between">
              <span>Chapters in {selectedSubject.name}</span>
              <span className="text-[10px] text-indigo-600 font-bold bg-indigo-50 px-2 py-0.5 rounded-full">
                NCERT
              </span>
            </div>

            <div className="space-y-1.5">
              {selectedSubject.chapters.map((ch) => (
                <button
                  key={ch.id}
                  onClick={() => {
                    setSelectedChapter(ch);
                    setSearchedTopicResult(null);
                    if (ch.concepts.length > 0) {
                      setSelectedConcept(ch.concepts[0]);
                    }
                  }}
                  className={`w-full p-3 rounded-2xl text-left transition flex items-center justify-between ${
                    selectedChapter.id === ch.id
                      ? "bg-indigo-50/80 border border-indigo-300 text-indigo-950 font-bold shadow-sm"
                      : "hover:bg-slate-50 text-slate-700 border border-transparent font-medium"
                  }`}
                >
                  <div>
                    <div className="text-xs font-bold">{ch.title}</div>
                    <div className="text-[10px] text-slate-500">{ch.ncertChapter}</div>
                  </div>
                  <ChevronRight className={`w-4 h-4 ${selectedChapter.id === ch.id ? "text-indigo-600" : "text-slate-400"}`} />
                </button>
              ))}
            </div>
          </div>

          {/* Concepts Selector under Chosen Chapter */}
          {selectedChapter.concepts.length > 0 && (
            <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-3">
              <div className="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center justify-between">
                <span>Concepts in {selectedChapter.title.split(" ")[0]}</span>
                <Layers className="w-3.5 h-3.5 text-slate-400" />
              </div>

              <div className="space-y-1.5">
                {selectedChapter.concepts.map((concept) => (
                  <button
                    key={concept.id}
                    onClick={() => {
                      setSelectedConcept(concept);
                      setSearchedTopicResult(null);
                    }}
                    className={`w-full p-3 rounded-2xl text-left text-xs transition flex items-center justify-between ${
                      activeConceptToDisplay.id === concept.id
                        ? "bg-emerald-50 border border-emerald-300 text-emerald-950 font-bold"
                        : "hover:bg-slate-50 text-slate-700 border border-transparent"
                    }`}
                  >
                    <div className="flex items-center space-x-2">
                      <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                      <span>{concept.name}</span>
                    </div>
                    <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Direct Navigation to Grader Button */}
          <div className="bg-gradient-to-br from-indigo-900 to-slate-900 p-5 rounded-3xl text-white shadow-lg space-y-3">
            <div className="flex items-center space-x-2 text-xs font-bold text-emerald-400 uppercase tracking-wider">
              <Sparkles className="w-4 h-4" />
              <span>Ready for Assessment?</span>
            </div>
            <p className="text-xs text-indigo-200">
              Test your subjective problem solving on <strong>{selectedChapter.title}</strong> with step-by-step scoring!
            </p>
            <button
              onClick={() => onNavigateToGrader(selectedChapter.id)}
              className="w-full py-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black rounded-xl text-xs transition flex items-center justify-center space-x-1.5 shadow-md"
            >
              <span>Go to AI Grader for this Chapter</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Right Column: Concept Teaching Pane */}
        <div className="lg:col-span-8 space-y-5">
          {/* Mode Switcher */}
          <div className="flex bg-slate-200/80 p-1.5 rounded-2xl">
            <button
              onClick={() => setLearningMode("standard")}
              className={`flex-1 py-2 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-2 ${
                learningMode === "standard"
                  ? "bg-white text-indigo-950 shadow-sm"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Curriculum & Internet Concept Guide</span>
            </button>
            <button
              onClick={() => setLearningMode("custom_ingest")}
              className={`flex-1 py-2 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-2 ${
                learningMode === "custom_ingest"
                  ? "bg-white text-indigo-950 shadow-sm"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Upload className="w-3.5 h-3.5" />
              <span>Learn from Notes PDF / YouTube Lecture</span>
            </button>
          </div>

          {learningMode === "custom_ingest" ? (
            /* Custom Ingest Mode */
            <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-5">
              <div>
                <h3 className="text-base font-bold text-slate-900">
                  Ingest External Study Material
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Paste a YouTube lecture link or paste notes from your PDF/Word document. EduAegis will synthesize it into plain English for Class 9.
                </p>
              </div>

              {/* Source Switcher */}
              <div className="flex space-x-2">
                <button
                  type="button"
                  onClick={() => setCustomInputType("youtube")}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition ${
                    customInputType === "youtube"
                      ? "bg-rose-50 text-rose-700 border border-rose-300"
                      : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                  }`}
                >
                  <Video className="w-3.5 h-3.5 text-rose-600" />
                  <span>YouTube Video Link</span>
                </button>
                <button
                  type="button"
                  onClick={() => setCustomInputType("document")}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition ${
                    customInputType === "document"
                      ? "bg-indigo-50 text-indigo-700 border border-indigo-300"
                      : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                  }`}
                >
                  <FileText className="w-3.5 h-3.5 text-indigo-600" />
                  <span>PDF / Notes Document</span>
                </button>
              </div>

              {customInputType === "youtube" ? (
                <div>
                  <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                    YouTube Educational Video URL
                  </label>
                  <div className="flex space-x-2">
                    <input
                      type="url"
                      value={youtubeUrl}
                      onChange={(e) => setYoutubeUrl(e.target.value)}
                      placeholder="https://www.youtube.com/watch?v=..."
                      className="flex-1 px-3.5 py-2 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                    />
                    <button
                      onClick={handleCustomIngest}
                      disabled={ingesting}
                      className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl transition shadow"
                    >
                      {ingesting ? "Analyzing Video..." : "Teach from Video"}
                    </button>
                  </div>
                </div>
              ) : (
                <div>
                  <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                    Paste Document Text or Lesson Notes
                  </label>
                  <textarea
                    rows={5}
                    value={documentText}
                    onChange={(e) => setDocumentText(e.target.value)}
                    placeholder="Paste textbook excerpt, teacher PDF summary, or study material here..."
                    className="w-full p-3 text-xs border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                  ></textarea>
                  <button
                    onClick={handleCustomIngest}
                    disabled={ingesting || !documentText.trim()}
                    className="mt-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl transition shadow"
                  >
                    {ingesting ? "Analyzing Document..." : "Teach from Notes"}
                  </button>
                </div>
              )}

              {/* Ingested Lesson Output */}
              {ingestedLesson && (
                <div className="mt-4 p-5 rounded-2xl bg-indigo-50/60 border border-indigo-200 space-y-3">
                  <div className="flex items-center justify-between">
                    <h4 className="text-sm font-bold text-indigo-950">{ingestedLesson.title}</h4>
                    <span className="text-[10px] font-bold bg-indigo-200 text-indigo-800 px-2 py-0.5 rounded-full">
                      Custom Ingested
                    </span>
                  </div>

                  {/* Audio Controls for Ingested Lesson */}
                  <div className="p-3 bg-white rounded-xl border border-indigo-100 flex items-center justify-between">
                    <div className="flex items-center space-x-2 text-xs font-bold text-indigo-900">
                      <Volume2 className="w-4 h-4 text-indigo-600 animate-pulse" />
                      <span>Audio Teacher Voice:</span>
                    </div>
                    <button
                      onClick={handleToggleAudio}
                      className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-bold flex items-center space-x-1.5 transition shadow"
                    >
                      {isPlayingAudio ? (
                        <>
                          <Pause className="w-3 h-3" />
                          <span>Pause Voice</span>
                        </>
                      ) : (
                        <>
                          <Play className="w-3 h-3" />
                          <span>Listen to Teacher</span>
                        </>
                      )}
                    </button>
                  </div>

                  <p className="text-xs text-slate-700 whitespace-pre-line leading-relaxed">
                    {ingestedLesson.explanation}
                  </p>
                </div>
              )}
            </div>
          ) : (
            /* Standard Concept Explanation */
            <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
              {/* Concept Title & Summary */}
              <div className="border-b border-slate-100 pb-4">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">
                    {selectedChapter.title}
                  </span>
                  <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-700">
                    {selectedSubject.name} • Class {selectedClass}th
                  </span>
                </div>
                <h2 className="text-xl font-black text-slate-900 mt-1">{activeConceptToDisplay.name}</h2>
                <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">{activeConceptToDisplay.summary}</p>
              </div>

              {/* Audio Teacher Player Bar (Speech Synthesis) */}
              <div className="p-4 rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-950 text-white shadow-md flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center space-x-3">
                  <div className="w-10 h-10 rounded-xl bg-indigo-600/60 flex items-center justify-center text-white">
                    <Volume2 className={`w-5 h-5 ${isPlayingAudio ? "text-emerald-400 animate-bounce" : "text-indigo-200"}`} />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-white flex items-center space-x-1.5">
                      <span>Audio Teacher Narration</span>
                      {isPlayingAudio && (
                        <span className="text-[10px] bg-emerald-500/30 text-emerald-300 px-2 py-0.5 rounded-full font-mono">
                          Playing...
                        </span>
                      )}
                    </div>
                    <div className="text-[11px] text-indigo-300">
                      Explains in plain conversational English like your best subject teacher
                    </div>
                  </div>
                </div>

                <div className="flex items-center space-x-2">
                  {/* Speed control */}
                  <select
                    value={speechRate}
                    onChange={(e) => setSpeechRate(Number(e.target.value))}
                    className="bg-slate-800 text-xs text-slate-200 px-2 py-1.5 rounded-lg border border-slate-700 outline-none"
                    title="Audio Speed"
                  >
                    <option value={0.85}>0.85x</option>
                    <option value={1.0}>1.0x Normal</option>
                    <option value={1.2}>1.2x Fast</option>
                  </select>

                  <button
                    onClick={handleToggleAudio}
                    className={`px-4 py-2 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition shadow-lg ${
                      isPlayingAudio
                        ? "bg-rose-600 hover:bg-rose-700 text-white"
                        : "bg-emerald-500 hover:bg-emerald-400 text-slate-950"
                    }`}
                  >
                    {isPlayingAudio ? (
                      <>
                        <Pause className="w-3.5 h-3.5" />
                        <span>Pause Audio</span>
                      </>
                    ) : (
                      <>
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span>Listen to Teacher</span>
                      </>
                    )}
                  </button>
                </div>
              </div>

              {/* Conversational Explanation */}
              <div className="space-y-3">
                <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center space-x-1.5">
                  <BookOpen className="w-3.5 h-3.5 text-indigo-600" />
                  <span>Teacher's Plain English Breakdown</span>
                </h4>
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-800 leading-relaxed font-sans">
                  {activeConceptToDisplay.teacherExplanation}
                </div>
              </div>

              {/* Everyday Analogies */}
              {activeConceptToDisplay.analogies && activeConceptToDisplay.analogies.length > 0 && (
                <div className="space-y-2">
                  <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                    Everyday Real-World Analogies:
                  </h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                    {activeConceptToDisplay.analogies.map((an, idx) => (
                      <div
                        key={idx}
                        className="p-3 bg-amber-50/70 border border-amber-200 rounded-xl text-[11px] text-amber-900 leading-snug"
                      >
                        💡 {an}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Key Formulas & Units */}
              {activeConceptToDisplay.keyFormulas && activeConceptToDisplay.keyFormulas.length > 0 && (
                <div className="p-4 rounded-2xl bg-indigo-50/60 border border-indigo-200 space-y-2">
                  <div className="text-xs font-bold text-indigo-950 uppercase tracking-wider">
                    Core Mathematical Formulas & SI Units:
                  </div>
                  <ul className="space-y-1 text-xs text-indigo-900 font-mono font-medium">
                    {activeConceptToDisplay.keyFormulas.map((f, i) => (
                      <li key={i} className="flex items-center space-x-2">
                        <span className="text-indigo-500 font-bold">›</span>
                        <span>{f}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Progressive Interactive Examples Loop */}
              <div className="space-y-3 pt-2 border-t border-slate-100">
                <div className="flex items-center justify-between">
                  <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center space-x-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
                    <span>Progressive Examples & Socratic Check</span>
                  </h4>
                  <span className="text-[11px] font-semibold text-slate-500">
                    Showing {Math.min(revealedExamplesCount, activeConceptToDisplay.examples.length)} of{" "}
                    {activeConceptToDisplay.examples.length} examples
                  </span>
                </div>

                <div className="space-y-3">
                  {activeConceptToDisplay.examples.slice(0, revealedExamplesCount).map((ex, index) => (
                    <div
                      key={index}
                      className="p-4 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-2"
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-xs font-bold text-indigo-700">{ex.title}</span>
                        <span className="text-[10px] font-semibold bg-slate-100 text-slate-600 px-2 py-0.5 rounded-full">
                          Example #{index + 1}
                        </span>
                      </div>
                      <div className="text-xs font-medium text-slate-800 bg-slate-50 p-2.5 rounded-xl border border-slate-200">
                        <strong>Scenario:</strong> {ex.scenario}
                      </div>
                      <div className="text-xs text-slate-600 leading-relaxed">
                        <strong>Explanation:</strong> {ex.explanation}
                      </div>
                    </div>
                  ))}
                </div>

                {/* Socratic Confirmation Box */}
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-3">
                  <div className="text-xs text-slate-700 text-center sm:text-left">
                    <span className="font-bold">Student Check:</span> Did you understand this concept, or would you like another example?
                  </div>
                  <div className="flex space-x-2">
                    {revealedExamplesCount < activeConceptToDisplay.examples.length && (
                      <button
                        onClick={() => setRevealedExamplesCount((prev) => prev + 1)}
                        className="px-3 py-1.5 text-xs font-bold text-indigo-700 bg-indigo-100 hover:bg-indigo-200 rounded-xl transition"
                      >
                        Explain with another real-life example
                      </button>
                    )}
                    <button
                      onClick={() => setStudentMasteryStatus("mastered")}
                      className={`px-3.5 py-1.5 text-xs font-bold rounded-xl transition flex items-center space-x-1 ${
                        studentMasteryStatus === "mastered"
                          ? "bg-emerald-600 text-white"
                          : "bg-emerald-100 hover:bg-emerald-200 text-emerald-800"
                      }`}
                    >
                      <CheckCircle className="w-3.5 h-3.5" />
                      <span>{studentMasteryStatus === "mastered" ? "Concept Understood!" : "I Understood!"}</span>
                    </button>
                  </div>
                </div>

                {studentMasteryStatus === "mastered" && (
                  <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-300 text-emerald-900 flex items-center justify-between">
                    <div className="text-xs font-medium">
                      🎉 <strong>Superb!</strong> You have confirmed understanding of <em>{activeConceptToDisplay.name}</em>.
                      Ready to test your subjective problem solving?
                    </div>
                    <button
                      onClick={() => onNavigateToGrader(selectedChapter.id)}
                      className="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl shadow transition"
                    >
                      Go to Grader ➔
                    </button>
                  </div>
                )}
              </div>

              {/* Authentic References & Links */}
              {activeConceptToDisplay.authenticReferences && activeConceptToDisplay.authenticReferences.length > 0 && (
                <div className="pt-3 border-t border-slate-100">
                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-500 mb-2">
                    Verified Authentic Curriculum References:
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {activeConceptToDisplay.authenticReferences.map((ref, i) => (
                      <a
                        key={i}
                        href={ref.url}
                        target="_blank"
                        rel="noreferrer"
                        className="text-[11px] font-semibold text-indigo-600 hover:text-indigo-800 bg-indigo-50 hover:bg-indigo-100 px-3 py-1 rounded-xl border border-indigo-200 flex items-center space-x-1.5 transition"
                      >
                        <span>{ref.title}</span>
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
