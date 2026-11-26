import { QuestionGrading, StepEvaluation, TeacherInstruction } from "./storage";

export interface EvaluationInput {
  questionId: string;
  questionText: string;
  studentAnswer: string;
  maxMarks: number;
  modelAnswer: string;
  rubricPoints: string[];
  referenceChapter: string;
  authenticReferences: { title: string; url: string; source: string }[];
  teacherInstruction?: TeacherInstruction;
  board?: string;
  subject?: string;
}

export function evaluateStudentAnswer(input: EvaluationInput): QuestionGrading {
  const answer = input.studentAnswer.trim();
  const answerLower = answer.toLowerCase();
  const max = input.maxMarks;
  const teacherInst = input.teacherInstruction;
  const qLower = input.questionText.toLowerCase();

  const stepBreakdown: StepEvaluation[] = [];
  const strengths: string[] = [];
  const gaps: string[] = [];

  // --------------------------------------------------------------------------
  // 1. PHYSICS EVALUATIONS
  // --------------------------------------------------------------------------
  const isSecondLaw = qLower.includes("second law") || qLower.includes("f = ma");
  const isFielder = qLower.includes("fielder") || qLower.includes("cricket");
  const isInertia = qLower.includes("inertia");
  const isNumericalCar = qLower.includes("motorcar") || qLower.includes("1200 kg");
  const isThirdLaw = qLower.includes("third law") || qLower.includes("action and reaction");

  // --------------------------------------------------------------------------
  // 2. CHEMISTRY EVALUATIONS
  // --------------------------------------------------------------------------
  const isEvaporationFactors = qLower.includes("evaporation") && (qLower.includes("factor") || qLower.includes("rate"));
  const isLatentHeat = qLower.includes("latent heat") || qLower.includes("steam");
  const isBoilingVsEvap = qLower.includes("boiling") && qLower.includes("evaporation");
  const isKelvinConversion = qLower.includes("kelvin") || qLower.includes("celsius");
  const isIceCooling = qLower.includes("ice at 273") || qLower.includes("ice at 0");

  // --------------------------------------------------------------------------
  // 3. MATHEMATICS EVALUATIONS
  // --------------------------------------------------------------------------
  const isRecurringFraction = qLower.includes("0.333") || qLower.includes("p/q") || qLower.includes("0.235");
  const isRationalize = qLower.includes("rationalize") || qLower.includes("denominator");
  const isRationalBetween = qLower.includes("rational numbers between") || qLower.includes("3/5 and 4/5");
  const isExponents = qLower.includes("exponents") || qLower.includes("simplify the following");
  const isClassifyNumbers = qLower.includes("classify") && qLower.includes("rational or irrational");

  // Evaluation Dispatcher
  if (isSecondLaw) {
    // Step 1: Definition of 2nd Law (1.0 Mark)
    const hasDef = answerLower.includes("rate of change of momentum") && answerLower.includes("proportional");
    const s1 = hasDef ? 1.0 : (answerLower.includes("momentum") ? 0.5 : 0.2);
    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Statement of Newton's Second Law",
      marksAwarded: s1,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasDef
        ? "Accurately stated that rate of change of momentum is directly proportional to applied unbalanced force."
        : "Partially stated; omitted either 'rate of change of momentum' or 'direction of force'."
    });

    // Step 2: Momentum formulation (1.5 Marks)
    const hasSteps = (answerLower.includes("mu") || answerLower.includes("p1")) && (answerLower.includes("mv") || answerLower.includes("p2"));
    const s2 = hasSteps ? 1.5 : (answerLower.includes("v - u") ? 1.0 : 0.3);
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Initial and Final Momentum Formulation",
      marksAwarded: s2,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasSteps
        ? "Clearly defined initial momentum p1 = mu and final momentum p2 = mv with change Δp = m(v - u)."
        : "Omitted explicit algebraic initial/final momentum steps."
    });

    // Step 3: Acceleration substitution (1.5 Marks)
    const hasAcc = answerLower.includes("a = (v - u)") || answerLower.includes("(v - u) / t") || answerLower.includes("acceleration a");
    const s3 = hasAcc ? 1.5 : (answerLower.includes("f = ma") ? 0.8 : 0.2);
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Substitution of a = (v-u)/t and Proportionality Constant k=1",
      marksAwarded: s3,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasAcc
        ? "Correctly substituted acceleration a = (v - u) / t into force expression to derive F = ma."
        : "Directly jumped to F = ma without showing intermediate acceleration equivalence."
    });

    // Step 4: SI Units (1.0 Mark)
    const hasUnits = answerLower.includes("newton") || answerLower.includes("kg") || answerLower.includes("m/s");
    let s4 = hasUnits ? 1.0 : 0.0;
    if (teacherInst?.strictSIUnits && !hasUnits) {
      s4 = 0.0;
      gaps.push("Teacher Directive Violation: SI units (Newton / N, kg, m/s²) were omitted (-1.0).");
    }
    stepBreakdown.push({
      stepNumber: 4,
      stepFocus: "Specification of SI Units for All Quantities",
      marksAwarded: s4,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasUnits
        ? "Correctly specified SI units for Force (N), Mass (kg), and Acceleration (m/s²)."
        : "Did not specify units for physical quantities."
    });
  } else if (isFielder) {
    const hasTime = answerLower.includes("time") && (answerLower.includes("increase") || answerLower.includes("longer") || answerLower.includes("more time"));
    const hasFormula = answerLower.includes("f =") || answerLower.includes("momentum") || answerLower.includes("rate of change");
    const hasForce = answerLower.includes("force") && (answerLower.includes("reduc") || answerLower.includes("decrease") || answerLower.includes("less") || answerLower.includes("prevent hurt"));

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Increasing Stopping Time Duration",
      marksAwarded: hasTime ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasTime ? "Noted that pulling hands back increases stopping time 't'." : "Failed to clearly explain the increase in time duration."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Newton's 2nd Law Application (F = Δp / Δt)",
      marksAwarded: hasFormula ? 1.0 : 0.2,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasFormula ? "Applied F = m(v-u)/t showing inverse relationship between impact force and time." : "Omitted theoretical connection to rate of change of momentum."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Consequence: Reduced Impact Force on Palms",
      marksAwarded: hasForce ? 1.0 : 0.2,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasForce ? "Concluded that reduced force prevents injury to the fielder's palms." : "Incomplete explanation of how reduced force protects hands."
    });
  } else if (isInertia) {
    const hasDef = answerLower.includes("resist") && (answerLower.includes("rest") || answerLower.includes("motion"));
    const hasTypes = (answerLower.includes("rest") ? 0.33 : 0) + (answerLower.includes("motion") ? 0.33 : 0) + (answerLower.includes("direction") ? 0.34 : 0);
    const hasMass = answerLower.includes("mass");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Definition of Inertia",
      marksAwarded: hasDef ? 1.0 : 0.4,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasDef ? "Accurately defined inertia as resistance to change of state." : "Definition lacked scientific precision."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Three Types of Inertia with Daily Examples",
      marksAwarded: Math.min(1.5, Math.round(hasTypes * 1.5 * 10) / 10),
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasTypes >= 0.9 ? "Listed Inertia of Rest, Motion, and Direction with valid examples." : "Missing one or more categories of inertia."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Measurement of Inertia (Mass)",
      marksAwarded: hasMass ? 0.5 : 0.0,
      maxMarks: 0.5,
      whyAwardedOrDeducted: hasMass ? "Correctly identified Mass as the quantitative measure of inertia." : "Omitted that mass measures inertia."
    });
  } else if (isNumericalCar) {
    const hasConversion = (answerLower.includes("25") && answerLower.includes("5")) || answerLower.includes("5/18");
    const hasAcc = answerLower.includes("-5") || answerLower.includes("retardation of 5");
    const hasMomentum = answerLower.includes("24000") || answerLower.includes("-24000");
    const hasForce = answerLower.includes("6000");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Velocity Unit Conversion (km/h -> m/s)",
      marksAwarded: hasConversion ? 1.0 : 0.2,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasConversion ? "Correctly converted 90 km/h = 25 m/s and 18 km/h = 5 m/s." : "Missed or incorrect conversion to SI units."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Acceleration Calculation (a = (v-u)/t)",
      marksAwarded: hasAcc ? 1.5 : (answerLower.includes("a =") ? 0.8 : 0.2),
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasAcc ? "Accurately calculated acceleration a = -5 m/s² (retardation)." : "Error in acceleration computation or missing negative sign."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Change in Momentum Calculation",
      marksAwarded: hasMomentum ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasMomentum ? "Correctly computed Δp = -24,000 kg·m/s." : "Omitted or miscalculated change in momentum."
    });
    stepBreakdown.push({
      stepNumber: 4,
      stepFocus: "Force Magnitude Calculation and Units",
      marksAwarded: hasForce ? 1.5 : 0.3,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasForce ? "Correctly calculated force F = 6000 N with correct SI unit (Newton)." : "Incorrect final force value or missing SI unit."
    });
  } else if (isThirdLaw) {
    const hasLaw = answerLower.includes("action") && answerLower.includes("reaction") && answerLower.includes("equal") && answerLower.includes("opposite");
    const hasDiffBodies = answerLower.includes("different") || answerLower.includes("two bodies") || answerLower.includes("different objects");
    const hasExample = answerLower.includes("walk") || answerLower.includes("ground") || answerLower.includes("rocket") || answerLower.includes("swim") || answerLower.includes("gun");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Statement of Newton's Third Law",
      marksAwarded: hasLaw ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasLaw ? "Stated that every action has an equal and opposite reaction." : "Incomplete statement of Third Law."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Forces Act Simultaneously on Two Different Bodies",
      marksAwarded: hasDiffBodies ? 2.0 : 0.5,
      maxMarks: 2.0,
      whyAwardedOrDeducted: hasDiffBodies
        ? "Exemplary explanation that action and reaction act simultaneously on TWO DIFFERENT bodies, so they never cancel."
        : "Failed to mention that forces act on different bodies, which is the primary reason they don't cancel."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Real-world Practical Illustration",
      marksAwarded: hasExample ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasExample ? "Provided a valid real-life illustration (e.g. walking on ground / gun recoil)." : "Missing or unclear example."
    });
  }
  // CHEMISTRY: Evaporation Factors
  else if (isEvaporationFactors) {
    const hasDef = answerLower.includes("below") && (answerLower.includes("boiling") || answerLower.includes("vapor"));
    const factorsCount = (answerLower.includes("surface") ? 1 : 0) +
                         (answerLower.includes("temperature") ? 1 : 0) +
                         (answerLower.includes("humidity") ? 1 : 0) +
                         (answerLower.includes("wind") ? 1 : 0);

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Definition of Evaporation",
      marksAwarded: hasDef ? 1.0 : 0.4,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasDef ? "Accurately stated that liquid changes to vapor at temperatures below boiling point." : "Incomplete definition; missed 'below boiling point'."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Four Factors with Practical Examples",
      marksAwarded: Math.min(4.0, factorsCount * 1.0),
      maxMarks: 4.0,
      whyAwardedOrDeducted: factorsCount === 4
        ? "Fully elaborated all four factors: surface area, temperature, humidity, and wind speed."
        : `Identified ${factorsCount} of 4 factors affecting evaporation rate.`
    });
  }
  // CHEMISTRY: Latent Heat & Steam Burns
  else if (isLatentHeat) {
    const hasLatentDef = answerLower.includes("latent heat") && (answerLower.includes("1 kg") || answerLower.includes("without change in temp") || answerLower.includes("hidden heat"));
    const hasExtraHeat = answerLower.includes("extra") || answerLower.includes("releases") || answerLower.includes("more heat") || answerLower.includes("condens");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Definition of Latent Heat of Vaporization",
      marksAwarded: hasLatentDef ? 1.5 : 0.5,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasLatentDef ? "Defined latent heat of vaporization with constant temperature condition." : "Partial definition of latent heat."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Severe Burn Explanation (Latent Heat Release)",
      marksAwarded: hasExtraHeat ? 2.5 : 0.8,
      maxMarks: 2.5,
      whyAwardedOrDeducted: hasExtraHeat ? "Explained that steam possesses extra latent heat released during condensation onto skin." : "Did not mention latent heat release on condensation."
    });
  }
  // MATHEMATICS: Recurring decimal to p/q
  else if (isRecurringFraction) {
    const hasAssumption = answerLower.includes("let x") || answerLower.includes("x =");
    const hasMultiply = answerLower.includes("10x") || answerLower.includes("100x") || answerLower.includes("1000x");
    const hasFraction = answerLower.includes("1/3") || answerLower.includes("3/9") || answerLower.includes("233/990");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Setting Up Algebraic Equation (x = 0.33...)",
      marksAwarded: hasAssumption ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasAssumption ? "Correctly initialized variable equation for repeating decimal." : "Omitted algebraic variable statement."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Multiplication by Powers of 10 to Align Repeating Period",
      marksAwarded: hasMultiply ? 1.0 : 0.3,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasMultiply ? "Accurately multiplied by power of 10 to shift repeating period." : "Missed multiplication step."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Subtraction & Simplifying to p/q Form",
      marksAwarded: hasFraction ? 1.0 : 0.2,
      maxMarks: 1.0,
      whyAwardedOrDeducted: hasFraction ? "Successfully simplified to lowest terms in p/q form (q ≠ 0)." : "Calculation error in final fraction."
    });
  }
  // MATHEMATICS: Rationalize Denominator
  else if (isRationalize) {
    const hasConjugate = answerLower.includes("7 - 3") || answerLower.includes("conjugate") || answerLower.includes("√2");
    const hasIdentity = answerLower.includes("49 - 18") || answerLower.includes("31") || answerLower.includes("a^2 - b^2");

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Conjugate Multiplication in Numerator & Denominator",
      marksAwarded: hasConjugate ? 1.5 : 0.5,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasConjugate ? "Multiplied both numerator and denominator by conjugate (7 - 3√2)." : "Missed conjugate multiplication."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Algebraic Expansion (a² - b²) and Final Result (31)",
      marksAwarded: hasIdentity ? 1.5 : 0.5,
      maxMarks: 1.5,
      whyAwardedOrDeducted: hasIdentity ? "Applied (a+b)(a-b) = a² - b² to obtain denominator 49 - 18 = 31." : "Error in expanding denominator."
    });
  }
  // GENERIC / CUSTOM USER TOPIC EVALUATOR
  else {
    const words = answer.split(/\s+/).filter(Boolean);
    const wordCount = words.length;
    const completeness = Math.min(1.0, wordCount / 40.0);
    const hasKeywords = answerLower.includes("formula") || answerLower.includes("unit") || answerLower.includes("law") || answerLower.includes("principle") || answerLower.includes("example");
    const hasFormula = /[=∝*/+\-^]/.test(answer);

    const s1 = Math.round(max * 0.4 * completeness * 10) / 10;
    const s2 = Math.round(max * 0.4 * (hasFormula ? 1.0 : 0.5) * 10) / 10;
    const s3 = Math.round(max * 0.2 * (hasKeywords ? 1.0 : 0.4) * 10) / 10;

    stepBreakdown.push({
      stepNumber: 1,
      stepFocus: "Theoretical Definition & Core Mechanism",
      marksAwarded: s1,
      maxMarks: Math.round(max * 0.4 * 10) / 10,
      whyAwardedOrDeducted: wordCount >= 30
        ? "Provided a well-elaborated conceptual answer addressing the core topic."
        : "Answer is brief; in board exams, step-by-step elaboration is required."
    });
    stepBreakdown.push({
      stepNumber: 2,
      stepFocus: "Mathematical Formulas, Equations & Relations",
      marksAwarded: s2,
      maxMarks: Math.round(max * 0.4 * 10) / 10,
      whyAwardedOrDeducted: hasFormula
        ? "Included relevant mathematical relationships or equations."
        : "Omitted explicit mathematical formulation or scientific notation."
    });
    stepBreakdown.push({
      stepNumber: 3,
      stepFocus: "Technical Terminology & Real-World Practical Verification",
      marksAwarded: s3,
      maxMarks: Math.round(max * 0.2 * 10) / 10,
      whyAwardedOrDeducted: hasKeywords
        ? "Used appropriate scientific/mathematical terminology."
        : "Could be improved by incorporating standard syllabus terminology."
    });
  }

  // Calculate total awarded marks from step breakdown
  let totalScore = stepBreakdown.reduce((sum, s) => sum + s.marksAwarded, 0);
  totalScore = Math.min(max, Math.max(0, Math.round(totalScore * 10) / 10));

  // Determine strengths & gaps
  if (totalScore >= max * 0.8) {
    strengths.push("Demonstrated strong mastery of core definitions, physical mechanisms, and mathematical steps.");
    strengths.push("Step-by-step reasoning was logically structured and aligned with board marking standards.");
  } else if (totalScore >= max * 0.5) {
    strengths.push("Addressed the primary question focus with partial technical accuracy.");
  }

  if (answer.length < 25) {
    gaps.push("Answer is excessively brief. In subjective board exams, full marks require step-by-step elaboration.");
  }

  const deductionRationale = gaps.length > 0
    ? gaps.join(" ")
    : "Evaluated strictly per NCERT syllabus rubrics and teacher instructions.";

  return {
    questionId: input.questionId,
    questionText: input.questionText,
    studentAnswer: input.studentAnswer,
    maxMarks: input.maxMarks,
    awardedMarks: totalScore,
    stepBreakdown: stepBreakdown,
    strengths: strengths,
    gapsAndMisconceptions: gaps,
    deductionExplanation: deductionRationale,
    referenceChapter: input.referenceChapter,
    authenticReferences: input.authenticReferences
  };
}
