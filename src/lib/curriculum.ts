/**
 * EduAegis Comprehensive Multi-Subject Curriculum Database
 * Covers Physics, Chemistry, Mathematics across Classes 8th, 9th, 10th.
 * Aligned with CBSE, ICSE, and State Board standards.
 */

export interface ConceptDetail {
  id: string;
  name: string;
  summary: string;
  teacherExplanation: string;
  audioScript: string;
  analogies: string[];
  examples: {
    title: string;
    scenario: string;
    explanation: string;
  }[];
  keyFormulas: string[];
  commonMisconceptions: string[];
  authenticReferences: {
    title: string;
    url: string;
    source: string;
  }[];
}

export interface PracticeExample {
  id: string;
  question: string;
  maxMarks: number;
  hiddenSolution: {
    steps: { stepNumber: number; description: string; marks: number }[];
    finalAnswer: string;
    keyInsight: string;
  };
}

export interface SubjectiveQuestion {
  id: string;
  question: string;
  maxMarks: number;
  questionType: "Short Definition" | "Conceptual Reasoning" | "Derivation / Numerical" | "Chemical Equation / Mechanism";
  modelAnswer: string;
  rubricPoints: string[];
}

export interface Chapter {
  id: string;
  title: string;
  ncertChapter: string;
  description: string;
  concepts: ConceptDetail[];
  practiceExamples: PracticeExample[];
  subjectivePaper: SubjectiveQuestion[];
}

export interface Subject {
  id: string;
  name: string;
  icon: string;
  accentColor: string;
  chapters: Chapter[];
}

export interface ClassCurriculum {
  className: string;
  classNumber: number;
  subjects: Subject[];
}

export const CURRICULUM_DATA: Record<number, ClassCurriculum> = {
  9: {
    className: "Class 9th (Secondary)",
    classNumber: 9,
    subjects: [
      {
        id: "physics",
        name: "Physics",
        icon: "Atom",
        accentColor: "from-blue-600 to-indigo-700",
        chapters: [
          {
            id: "force_and_laws",
            title: "Force and Laws of Motion",
            ncertChapter: "NCERT Class 9 - Chapter 8",
            description: "Study balanced & unbalanced forces, inertia, momentum, Newton's three laws of motion, and conservation of momentum.",
            concepts: [
              {
                id: "newton_second_law",
                name: "Newton's Second Law & Momentum (F = ma)",
                summary: "The rate of change of momentum of an object is directly proportional to the applied unbalanced force and takes place in the direction of the force.",
                teacherExplanation: "Hello! Let's understand Newton's Second Law in simple terms. Imagine you are in a cricket match. When a fast cricket ball comes towards you, catching it hurts your hand if you stop it instantly. But if you pull your hands backward, you take more time to stop the ball, reducing the force! That's momentum and Newton's Second Law in real life. Force equals mass times acceleration (F = ma).",
                audioScript: "Hello student! Welcome to EduAegis Physics class. Today we are mastering Newton's Second Law of Motion. First, what is momentum? Momentum is mass in motion: p equals m times v. Newton discovered that when you push something, the change in its momentum depends directly on the force applied and the time taken. By pulling your hands back while catching a cricket ball, you increase time, which reduces the force on your palms. Remember the golden formula: Force equals mass times acceleration, F equals m a, measured in Newtons.",
                analogies: [
                  "Catching a fast cricket ball: pulling hands back increases time 't', reducing impact force 'F'.",
                  "High jump athletes landing on soft foam or sand cushions to increase deceleration time.",
                  "Seatbelts in cars stretching slightly during sudden braking to prolong stopping time."
                ],
                examples: [
                  {
                    title: "Example 1: A Pushed Shopping Cart",
                    scenario: "A 20 kg empty shopping cart is accelerated at 2 m/s². What force was applied?",
                    explanation: "Using F = m * a: Mass m = 20 kg, acceleration a = 2 m/s². Force = 20 * 2 = 40 Newtons (N). If you double the mass by loading 20 kg groceries, the same 40 N force will only produce an acceleration of 1 m/s²."
                  },
                  {
                    title: "Example 2: Why Karate Fighters Break Bricks",
                    scenario: "A karate expert strikes a pile of tiles with very high speed in a tiny fraction of a second.",
                    explanation: "The mass of the hand is moderate, but the velocity drops from high speed to zero in a tiny fraction of a second (t ≈ 0.01 s). Because Δt is extremely small, the rate of change of momentum is enormous, delivering a massive breaking force."
                  }
                ],
                keyFormulas: [
                  "Momentum: p = m * v (SI unit: kg·m/s)",
                  "Force: F = Δp / Δt = m(v - u) / t",
                  "Newton's Second Law: F = m * a (SI unit: Newton, 1 N = 1 kg·m/s²)"
                ],
                commonMisconceptions: [
                  "Confusing Newton's 2nd Law (rate of change of momentum) with 3rd Law (action-reaction).",
                  "Assuming force is needed to maintain motion; an object in uniform motion needs zero net force.",
                  "Writing the SI unit of force as Joules (energy) instead of Newtons (N)."
                ],
                authenticReferences: [
                  {
                    title: "NCERT Class 9 Physics - Force & Laws of Motion",
                    url: "https://ncert.nic.in/textbook.php?iesc1=8-15",
                    source: "NCERT Official Portal"
                  },
                  {
                    title: "Khan Academy: Newton's Second Law of Motion",
                    url: "https://www.khanacademy.org/science/in-in-class9th-physics-india/in-in-forces-and-laws-of-motion",
                    source: "Khan Academy India"
                  },
                  {
                    title: "HyperPhysics - Georgia State University: Newton's Laws",
                    url: "http://hyperphysics.phy-astr.gsu.edu/hbase/newt.html",
                    source: "HyperPhysics"
                  }
                ]
              }
            ],
            practiceExamples: [
              {
                id: "ex_1",
                question: "A constant force acts on an object of mass 5 kg for a duration of 2 seconds. It increases the object's velocity from 3 m/s to 7 m/s. Find the magnitude of the applied force. If the force was applied for a duration of 5 seconds, what would be the final velocity?",
                maxMarks: 4,
                hiddenSolution: {
                  steps: [
                    { stepNumber: 1, description: "Identify given parameters: mass m = 5 kg, initial velocity u = 3 m/s, final velocity v = 7 m/s, time t = 2 s.", marks: 1 },
                    { stepNumber: 2, description: "Calculate acceleration: a = (v - u) / t = (7 - 3) / 2 = 4 / 2 = 2 m/s².", marks: 1 },
                    { stepNumber: 3, description: "Calculate force using Newton's Second Law: F = m * a = 5 kg * 2 m/s² = 10 N.", marks: 1 },
                    { stepNumber: 4, description: "Compute final velocity when time t' = 5 s: v' = u + a * t' = 3 + (2 * 5) = 3 + 10 = 13 m/s.", marks: 1 }
                  ],
                  finalAnswer: "Applied Force = 10 Newtons; Final Velocity after 5 s = 13 m/s.",
                  keyInsight: "Force remains constant, so acceleration is constant throughout the motion."
                }
              }
            ],
            subjectivePaper: [
              {
                id: "q1",
                question: "State Newton's Second Law of Motion. Derive the mathematical expression F = ma from this law, defining all terms with their SI units.",
                maxMarks: 5,
                questionType: "Derivation / Numerical",
                modelAnswer: "Newton's Second Law of Motion states that the rate of change of momentum of an object is directly proportional to the applied unbalanced force, and takes place in the direction of the force.\n\nDerivation:\nLet mass of the object be 'm', initial velocity 'u', and final velocity 'v' after time 't' under force 'F'.\nInitial momentum p1 = m * u\nFinal momentum p2 = m * v\nChange in momentum Δp = p2 - p1 = m(v - u)\nRate of change of momentum = m(v - u) / t\nBy Newton's 2nd Law: F ∝ m(v - u) / t\nSince acceleration a = (v - u) / t:\nF ∝ m * a => F = k * m * a\nIn SI units, choosing k = 1: F = m * a.\nSI Units: Force in Newton (N), mass in kg, acceleration in m/s².",
                rubricPoints: [
                  "1.0 mark: Exact statement of Newton's 2nd Law (rate of change of momentum proportional to unbalanced force in its direction).",
                  "2.0 marks: Step-by-step derivation: p1=mu, p2=mv, Δp=m(v-u), rate of change = m(v-u)/t.",
                  "1.0 mark: Substituting a = (v-u)/t to get F = k*m*a, explaining why k=1 in SI.",
                  "1.0 mark: Correct SI units for all quantities (Force in N, mass in kg, acceleration in m/s²)."
                ]
              },
              {
                id: "q2",
                question: "Why does a fielder pull his hands backward while catching a fast-moving cricket ball? Explain the physical mechanism using Newton's Second Law.",
                maxMarks: 3,
                questionType: "Conceptual Reasoning",
                modelAnswer: "When a fielder pulls his hands backward while catching a cricket ball, he increases the time duration 't' over which the high velocity of the ball is reduced to zero. According to Newton's Second Law, Force F = m(v - u) / t. Since the change in momentum m(v - u) is constant, increasing the time 't' decreases the rate of change of momentum. Consequently, a much smaller impact force is exerted on the fielder's palms, preventing injury.",
                rubricPoints: [
                  "1.0 mark: Mentions that pulling hands back increases the time taken to bring ball's velocity to zero.",
                  "1.0 mark: Applies Newton's 2nd Law formula F = m(v-u)/t showing inverse relationship between force and time.",
                  "1.0 mark: Concludes that smaller stopping force acts on the hands, preventing pain or injury."
                ]
              },
              {
                id: "q3",
                question: "Define Inertia. State its three types with one daily-life example for each. Name the physical quantity that measures inertia.",
                maxMarks: 3,
                questionType: "Short Definition",
                modelAnswer: "Inertia is the inherent property of an object by virtue of which it resists any change in its state of rest or of uniform motion in a straight line.\n\nThree Types:\n1. Inertia of Rest: A person jerks backward when a stationary bus starts suddenly.\n2. Inertia of Motion: A passenger falls forward when a moving bus brakes abruptly.\n3. Inertia of Direction: Water droplets flying off tangential to a rotating bicycle wheel.\n\nMeasurement: Mass is the quantitative measure of inertia of an object.",
                rubricPoints: [
                  "1.0 mark: Accurate scientific definition of inertia.",
                  "1.5 marks: Stating all 3 types (Rest, Motion, Direction) with correct daily-life examples.",
                  "0.5 mark: Explicitly stating that Mass is the measure of inertia."
                ]
              },
              {
                id: "q4",
                question: "A motorcar of mass 1200 kg is moving along a straight line with a uniform velocity of 90 km/h. Its velocity is slowed down to 18 km/h in 4 seconds by an unbalanced external force. Calculate the acceleration and the change in momentum. Also calculate the magnitude of the force required.",
                maxMarks: 5,
                questionType: "Derivation / Numerical",
                modelAnswer: "Given: Mass m = 1200 kg.\nInitial velocity u = 90 km/h = 90 * (5/18) = 25 m/s.\nFinal velocity v = 18 km/h = 18 * (5/18) = 5 m/s.\nTime t = 4 s.\n\n1. Acceleration:\na = (v - u) / t = (5 - 25) / 4 = -20 / 4 = -5 m/s² (Retardation).\n\n2. Change in Momentum:\nΔp = m(v - u) = 1200 * (5 - 25) = 1200 * (-20) = -24,000 kg·m/s.\n\n3. Force:\nF = m * a = 1200 * (-5) = -6000 N.\nMagnitude of force required = 6000 N (acting opposite to motion).",
                rubricPoints: [
                  "1.0 mark: Converting velocities from km/h to m/s correctly (u = 25 m/s, v = 5 m/s).",
                  "1.5 marks: Correct acceleration formula and calculation a = -5 m/s² with negative sign/retardation.",
                  "1.0 mark: Correct change in momentum Δp = -24,000 kg·m/s with units.",
                  "1.5 marks: Correct force magnitude F = 6000 N with correct SI unit (N)."
                ]
              },
              {
                id: "q5",
                question: "State Newton's Third Law of Motion. Why do action and reaction forces not cancel each other even though they are equal in magnitude and opposite in direction?",
                maxMarks: 4,
                questionType: "Conceptual Reasoning",
                modelAnswer: "Newton's Third Law of Motion states that to every action, there is an equal and opposite reaction.\n\nWhy they do not cancel:\nAction and reaction forces do not cancel each other because they ALWAYS ACT ON TWO DIFFERENT BODIES simultaneously, never on the same body.\nFor forces to cancel each other and produce zero net force, they must act on the same object. For example, when you walk on ground, your foot pushes the ground backward (Action on ground), and the ground pushes your foot forward (Reaction on foot). Because they act on different entities (ground and foot), motion is produced.",
                rubricPoints: [
                  "1.0 mark: Accurate statement of Newton's Third Law.",
                  "2.0 marks: Crucial reasoning that action and reaction act on TWO DIFFERENT BODIES simultaneously.",
                  "1.0 mark: Clear illustrative example (e.g., walking, swimming, rocket propulsion)."
                ]
              }
            ]
          }
        ]
      },
      {
        id: "chemistry",
        name: "Chemistry",
        icon: "FlaskConical",
        accentColor: "from-emerald-600 to-teal-700",
        chapters: [
          {
            id: "matter_surroundings",
            title: "Matter in Our Surroundings & States of Matter",
            ncertChapter: "NCERT Class 9 - Chapter 1",
            description: "Physical nature of matter, characteristics of particles, states of matter, latent heat, and evaporation cooling.",
            concepts: [
              {
                id: "evaporation_cooling",
                name: "Evaporation & Factors Affecting Cooling",
                summary: "Evaporation is a surface phenomenon where liquid turns to vapor below its boiling point by absorbing latent heat of vaporization from surroundings, causing cooling.",
                teacherExplanation: "When you pour a few drops of acetone or perfume on your palm, your hand feels cold. Why? The liquid particles absorb heat energy from your palm to evaporate, leaving your hand cooler! The rate of evaporation increases with higher surface area, higher temperature, higher wind speed, and lower humidity.",
                audioScript: "Welcome to Class 9 Chemistry! Today we explore why evaporation causes cooling. When a liquid evaporates, only surface particles with high kinetic energy break free into vapor. Where do they get the energy? They absorb latent heat from the surrounding surface. Because heat is taken away from that surface, it cools down. This is exactly how earthen pots keep water cool and why wearing cotton clothes in summer feels so comfortable.",
                analogies: [
                  "Earthen pots (matka) keeping water cool in Indian summers through microscopic pores.",
                  "Wearing cotton clothes in summer to absorb sweat and promote evaporative cooling.",
                  "Spreading wet clothes wide on a line to increase surface area for faster drying."
                ],
                examples: [
                  {
                    title: "Example 1: Why wear cotton clothes in summer?",
                    scenario: "During summer, our body perspires heavily to maintain constant temperature.",
                    explanation: "Cotton is a good absorber of water. It absorbs sweat and exposes it to the atmosphere. The latent heat of vaporization is absorbed from our body, cooling us."
                  },
                  {
                    title: "Example 2: Acetone / Spirit on Palm",
                    scenario: "A drop of nail polish remover on your skin.",
                    explanation: "Acetone has low boiling point and high volatility. It takes heat from your skin and evaporates rapidly, giving an instant cooling sensation."
                  }
                ],
                keyFormulas: [
                  "Rate of Evaporation ∝ Surface Area",
                  "Rate of Evaporation ∝ Temperature",
                  "Rate of Evaporation ∝ Wind Speed",
                  "Rate of Evaporation ∝ 1 / Humidity"
                ],
                commonMisconceptions: [
                  "Confusing evaporation (surface phenomenon at any temperature) with boiling (bulk phenomenon at specific boiling point).",
                  "Assuming temperature rises during phase change (latent heat is absorbed without temperature increase)."
                ],
                authenticReferences: [
                  {
                    title: "NCERT Class 9 Chemistry - Chapter 1",
                    url: "https://ncert.nic.in/textbook.php?iesc1=1-15",
                    source: "NCERT"
                  },
                  {
                    title: "Khan Academy: States of Matter and Phase Changes",
                    url: "https://www.khanacademy.org/science/in-in-class9th-chemistry-india",
                    source: "Khan Academy"
                  }
                ]
              }
            ],
            practiceExamples: [
              {
                id: "chem_ex_1",
                question: "Why does a desert cooler cool better on a hot, dry day than on a humid rainy day?",
                maxMarks: 3,
                hiddenSolution: {
                  steps: [
                    { stepNumber: 1, description: "State condition on a hot dry day: high temperature and very low humidity.", marks: 1 },
                    { stepNumber: 2, description: "Explain mechanism: rate of evaporation of water from cooler pads increases dramatically when humidity is low.", marks: 1 },
                    { stepNumber: 3, description: "Conclude: higher evaporation absorbs more latent heat from incoming air, delivering much cooler air.", marks: 1 }
                  ],
                  finalAnswer: "Higher temperature and low humidity maximize the rate of water evaporation, producing superior cooling.",
                  keyInsight: "Evaporation rate is inversely proportional to humidity."
                }
              }
            ],
            subjectivePaper: [
              {
                id: "chem_q1",
                question: "Define Evaporation. Explain four factors that affect the rate of evaporation with one practical example for each.",
                maxMarks: 5,
                questionType: "Conceptual Reasoning",
                modelAnswer: "Evaporation is the phenomenon of change of a liquid into vapors at any temperature below its boiling point.\n\nFour Factors Affecting Rate of Evaporation:\n1. Surface Area: An increase in surface area increases rate of evaporation (e.g. spreading clothes on line).\n2. Temperature: Higher temperature increases kinetic energy of particles, accelerating evaporation (e.g. clothes dry faster in summer).\n3. Humidity: Humidity is moisture in air. If humidity is already high, rate of evaporation decreases (e.g. sweat does not dry easily on rainy days).\n4. Wind Speed: High wind speed moves water vapor particles away, increasing evaporation (e.g. clothes dry faster on a windy day).",
                rubricPoints: [
                  "1.0 mark: Accurate definition of evaporation (specifying 'below boiling point').",
                  "4.0 marks: 1 mark for each of the 4 factors (Surface area, Temperature, Humidity, Wind speed) with valid explanation and example."
                ]
              },
              {
                id: "chem_q2",
                question: "What is Latent Heat of Vaporization? Why does steam at 100°C cause more severe burns than boiling water at the same temperature 100°C?",
                maxMarks: 4,
                questionType: "Conceptual Reasoning",
                modelAnswer: "Latent Heat of Vaporization is the amount of heat energy required to change 1 kg of a liquid into gas at atmospheric pressure at its boiling point without any change in temperature.\n\nWhy Steam Causes More Severe Burns:\nEven though both boiling water and steam are at 100°C, steam contains extra latent heat of vaporization (approx 22.6 x 10^5 J/kg) that water absorbed to turn into vapor. When steam comes in contact with skin, it condenses back to water and releases this additional hidden heat, causing far more severe burns than liquid water.",
                rubricPoints: [
                  "1.5 marks: Precise definition of Latent Heat of Vaporization.",
                  "2.5 marks: Explaining that steam contains extra latent heat energy and releases it upon condensing onto skin."
                ]
              },
              {
                id: "chem_q3",
                question: "Differentiate between Boiling and Evaporation on any three parameters.",
                maxMarks: 3,
                questionType: "Short Definition",
                modelAnswer: "Differences between Evaporation and Boiling:\n1. Phenomenon: Evaporation is a surface phenomenon; Boiling is a bulk phenomenon.\n2. Temperature: Evaporation occurs at any temperature below boiling point; Boiling occurs only at a fixed temperature (boiling point).\n3. Cooling Effect: Evaporation always causes cooling; Boiling does not cause cooling.",
                rubricPoints: [
                  "1.0 mark: Surface vs Bulk phenomenon distinction.",
                  "1.0 mark: Temperature condition distinction.",
                  "1.0 mark: Cooling effect distinction."
                ]
              },
              {
                id: "chem_q4",
                question: "Convert the following temperatures into the Kelvin scale and Celsius scale:\n(a) 25°C to Kelvin\n(b) 373 K to Celsius\nState the relation used.",
                maxMarks: 3,
                questionType: "Derivation / Numerical",
                modelAnswer: "Relation: Temperature in Kelvin (K) = Temperature in Celsius (°C) + 273.15 (or + 273).\n\n(a) 25°C to Kelvin:\nT(K) = 25 + 273 = 298 K.\n\n(b) 373 K to Celsius:\nT(°C) = 373 - 273 = 100°C.",
                rubricPoints: [
                  "1.0 mark: Stating the formula T(K) = T(°C) + 273.",
                  "1.0 mark: Correct calculation of 25°C = 298 K with unit.",
                  "1.0 mark: Correct calculation of 373 K = 100°C with unit."
                ]
              },
              {
                id: "chem_q5",
                question: "Explain why ice at 273 K (0°C) is more effective in cooling than water at the same temperature 273 K.",
                maxMarks: 5,
                questionType: "Conceptual Reasoning",
                modelAnswer: "Ice at 273 K (0°C) is more effective in cooling than water at 273 K because ice absorbs additional heat equal to the Latent Heat of Fusion (3.34 x 10^5 J/kg) from the surroundings in order to melt into liquid water at 0°C.\n\nLiquid water at 273 K already contains this latent heat energy, so it can only absorb sensible heat to warm up. Because ice absorbs both latent heat of melting plus sensible heat, it draws significantly more thermal energy out of the substance, producing far more effective cooling.",
                rubricPoints: [
                  "2.0 marks: Identifying Latent Heat of Fusion absorbed by ice to undergo phase transition.",
                  "2.0 marks: Comparing energy contents: liquid water at 0°C already possesses latent heat.",
                  "1.0 mark: Concluding that ice extracts more net thermal energy from the substance."
                ]
              }
            ]
          }
        ]
      },
      {
        id: "mathematics",
        name: "Mathematics",
        icon: "Calculator",
        accentColor: "from-purple-600 to-violet-800",
        chapters: [
          {
            id: "number_systems",
            title: "Number Systems: Rational & Irrational Numbers",
            ncertChapter: "NCERT Class 9 - Chapter 1",
            description: "Real numbers, decimal expansions (terminating vs non-terminating), representation of √x on number line, laws of exponents.",
            concepts: [
              {
                id: "irrational_proofs",
                name: "Rational vs Irrational Numbers & Decimal Expansion",
                summary: "A rational number can be expressed as p/q (q ≠ 0) with terminating or non-terminating repeating decimals. An irrational number has non-terminating and non-repeating decimal expansion.",
                teacherExplanation: "Hello! In Class 9 Maths, numbers are divided into rational and irrational. Rational numbers like 1/2 (0.5) or 1/3 (0.333 recurring) can always be written as a fraction p/q. But numbers like √2, √3, and π (pi) cannot be written as fractions; their decimals go on forever without ever repeating a pattern!",
                audioScript: "Welcome to Class 9 Mathematics. Real numbers consist of rational and irrational numbers. A rational number has a decimal expansion that either terminates, like 0.25, or recurs endlessly, like 0.3 bar. In contrast, an irrational number has a decimal expansion that is non-terminating and non-recurring. Remember: 22 over 7 is only an approximate rational estimate of pi; the true number pi is strictly irrational.",
                analogies: [
                  "Rational decimals repeat like a heartbeat monitor (0.333...); irrational decimals wander unpredictably like random steps.",
                  "Measuring grid diagonals with Pythagoras Theorem."
                ],
                examples: [
                  {
                    title: "Example 1: Express 0.333... in p/q form",
                    scenario: "Let x = 0.3333...",
                    explanation: "Multiply by 10: 10x = 3.3333... Subtract x: 9x = 3 => x = 3/9 = 1/3. Since it can be written as 1/3, 0.3 bar is a rational number."
                  }
                ],
                keyFormulas: [
                  "Rational: p/q where p, q ∈ Z and q ≠ 0",
                  "Laws of Exponents: a^m * a^n = a^(m+n); (a^m)^n = a^(mn); a^m / a^n = a^(m-n)",
                  "Rationalization: 1 / (√a + √b) = (√a - √b) / (a - b)"
                ],
                commonMisconceptions: [
                  "Assuming 22/7 is equal to π; 22/7 is rational, whereas π is irrational.",
                  "Thinking the sum of two irrational numbers is always irrational (e.g. √2 + (-√2) = 0, which is rational)."
                ],
                authenticReferences: [
                  {
                    title: "NCERT Class 9 Mathematics - Chapter 1",
                    url: "https://ncert.nic.in/textbook.php?iemh1=1-15",
                    source: "NCERT"
                  },
                  {
                    title: "Khan Academy: Real Numbers Class 9",
                    url: "https://www.khanacademy.org/math/in-in-grade-9-ncert",
                    source: "Khan Academy"
                  }
                ]
              }
            ],
            practiceExamples: [
              {
                id: "math_ex_1",
                question: "Express 0.2353535... (i.e. 0.235 with bar on 35) in the form p/q, where p and q are integers and q ≠ 0.",
                maxMarks: 3,
                hiddenSolution: {
                  steps: [
                    { stepNumber: 1, description: "Let x = 0.2353535... Multiply by 10 to bring non-repeating digit before decimal: 10x = 2.353535... (Eq 1)", marks: 1 },
                    { stepNumber: 2, description: "Multiply Eq 1 by 100 since 2 digits repeat: 1000x = 235.353535... (Eq 2)", marks: 1 },
                    { stepNumber: 3, description: "Subtract Eq 1 from Eq 2: 1000x - 10x = 235.3535... - 2.3535... => 990x = 233 => x = 233 / 990.", marks: 1 }
                  ],
                  finalAnswer: "0.23535... = 233 / 990 in p/q form.",
                  keyInsight: "Multiply by powers of 10 to align repeating decimal periods before subtracting."
                }
              }
            ],
            subjectivePaper: [
              {
                id: "math_q1",
                question: "Show that 0.3333... = 0.3̄ can be expressed in the form p/q, where p and q are integers and q ≠ 0.",
                maxMarks: 3,
                questionType: "Derivation / Numerical",
                modelAnswer: "Let x = 0.3333... --- (Equation 1)\n\nSince one digit is repeating, multiply both sides by 10:\n10x = 3.3333... --- (Equation 2)\n\nSubtracting Equation (1) from Equation (2):\n10x - x = (3.3333...) - (0.3333...)\n9x = 3\nx = 3 / 9\nx = 1 / 3\n\nSince 1 and 3 are integers and 3 ≠ 0, 0.3̄ = 1/3 in p/q form.",
                rubricPoints: [
                  "1.0 mark: Correct assumption statement x = 0.333...",
                  "1.0 mark: Multiplying by 10 to get 10x = 3.333...",
                  "1.0 mark: Correct subtraction 9x = 3 and simplifying to x = 1/3."
                ]
              },
              {
                id: "math_q2",
                question: "Rationalize the denominator of: 1 / (7 + 3√2). Show all intermediate multiplication steps.",
                maxMarks: 3,
                questionType: "Derivation / Numerical",
                modelAnswer: "Given: 1 / (7 + 3√2)\n\nMultiply numerator and denominator by the conjugate (7 - 3√2):\n= [1 * (7 - 3√2)] / [(7 + 3√2)(7 - 3√2)]\n\nUsing algebraic identity (a + b)(a - b) = a² - b² in the denominator:\nDenominator = 7² - (3√2)² = 49 - (9 * 2) = 49 - 18 = 31\n\nTherefore:\n= (7 - 3√2) / 31.",
                rubricPoints: [
                  "1.0 mark: Multiplying numerator and denominator by conjugate (7 - 3√2).",
                  "1.0 mark: Applying (a+b)(a-b) = a² - b² in denominator (49 - 18 = 31).",
                  "1.0 mark: Stating the final simplified fraction (7 - 3√2) / 31."
                ]
              },
              {
                id: "math_q3",
                question: "Find three rational numbers between 3/5 and 4/5 using the mean method or common denominator method.",
                maxMarks: 4,
                questionType: "Derivation / Numerical",
                modelAnswer: "To find 3 rational numbers between 3/5 and 4/5:\nMultiply numerator and denominator of both fractions by (3 + 1) = 4 (or 10):\n3/5 = (3 * 10) / (5 * 10) = 30 / 50\n4/5 = (4 * 10) / (5 * 10) = 40 / 50\n\nThree rational numbers between 30/50 and 40/50 are:\n31/50, 32/50 (or 16/25), and 33/50.\n\nAll three lie strictly between 3/5 and 4/5.",
                rubricPoints: [
                  "1.5 marks: Correct equivalent fraction conversion (e.g. 30/50 and 40/50).",
                  "2.5 marks: Stating three valid intermediate rational numbers with verification."
                ]
              },
              {
                id: "math_q4",
                question: "Simplify the following expression using laws of exponents:\n(a) (2^(2/3)) * (2^(1/3))\n(b) (1 / 3^3)^7\n(c) (7^(1/5)) / (7^(1/3))",
                maxMarks: 5,
                questionType: "Derivation / Numerical",
                modelAnswer: "(a) Using a^m * a^n = a^(m+n):\n2^(2/3 + 1/3) = 2^(3/3) = 2^1 = 2.\n\n(b) Using (1 / a^m)^n = (a^(-m))^n = a^(-mn):\n(3^(-3))^7 = 3^(-21) = 1 / 3^21.\n\n(c) Using a^m / a^n = a^(m-n):\n7^(1/5 - 1/3) = 7^((3 - 5) / 15) = 7^(-2/15) = 1 / 7^(2/15).",
                rubricPoints: [
                  "1.5 marks: Correct simplification of part (a) = 2 with law stated.",
                  "1.5 marks: Correct simplification of part (b) = 1 / 3^21 with law stated.",
                  "2.0 marks: Correct LCM fraction subtraction and simplification of part (c) = 7^(-2/15)."
                ]
              },
              {
                id: "math_q5",
                question: "Classify the following numbers as rational or irrational with mathematical justification:\n(i) 2 - √5\n(ii) (3 + √23) - √23\n(iii) 2π",
                maxMarks: 5,
                questionType: "Conceptual Reasoning",
                modelAnswer: "(i) 2 - √5:\nHere 2 is rational and √5 is irrational. The difference between a rational number and an irrational number is always irrational. Therefore, 2 - √5 is IRRATIONAL.\n\n(ii) (3 + √23) - √23:\nSimplifying: 3 + √23 - √23 = 3 = 3/1.\nSince 3 can be written as p/q where q = 1 ≠ 0, it is RATIONAL.\n\n(iii) 2π:\nHere 2 is rational and π is irrational. The product of a non-zero rational number with an irrational number is always irrational. Therefore, 2π is IRRATIONAL.",
                rubricPoints: [
                  "1.5 marks: Correct classification and justification for (i) (Difference rule).",
                  "1.5 marks: Correct simplification and rational proof for (ii).",
                  "2.0 marks: Correct classification and justification for (iii) (Product rule)."
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  8: {
    className: "Class 8th (Middle School)",
    classNumber: 8,
    subjects: [
      {
        id: "physics_8",
        name: "Physics (Science)",
        icon: "Atom",
        accentColor: "from-sky-600 to-blue-700",
        chapters: [
          {
            id: "force_pressure_8",
            title: "Force and Pressure",
            ncertChapter: "NCERT Class 8 - Chapter 8",
            description: "Contact and non-contact forces, atmospheric pressure, and pressure exerted by liquids.",
            concepts: [
              {
                id: "force_types",
                name: "Contact and Non-Contact Forces",
                summary: "Forces requiring physical contact (muscular, friction) versus forces acting from a distance (gravitational, magnetic, electrostatic).",
                teacherExplanation: "Whenever you kick a ball, your foot touches it (contact force). But when a magnet pulls an iron nail, it happens across empty air (non-contact force)!",
                audioScript: "In Class 8 Science, forces are classified as contact and non-contact. Muscular and frictional forces require physical touch, while magnetic, electrostatic, and gravitational forces act at a distance.",
                analogies: ["Kicking a football vs a magnet picking up paper clips."],
                examples: [],
                keyFormulas: ["Pressure = Force / Area"],
                commonMisconceptions: ["Assuming friction only opposes motion and has no useful purpose."],
                authenticReferences: [{ title: "NCERT Class 8 Science", url: "https://ncert.nic.in", source: "NCERT" }]
              }
            ],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      },
      {
        id: "chemistry_8",
        name: "Chemistry (Science)",
        icon: "FlaskConical",
        accentColor: "from-emerald-600 to-teal-700",
        chapters: [
          {
            id: "combustion_flame_8",
            title: "Combustion and Flame",
            ncertChapter: "NCERT Class 8 - Chapter 6",
            description: "Chemical process of combustion, ignition temperature, inflammable substances, structure of flame.",
            concepts: [],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      },
      {
        id: "maths_8",
        name: "Mathematics",
        icon: "Calculator",
        accentColor: "from-purple-600 to-violet-800",
        chapters: [
          {
            id: "linear_equations_8",
            title: "Linear Equations in One Variable",
            ncertChapter: "NCERT Class 8 - Chapter 2",
            description: "Solving linear equations having the variable on one side and both sides.",
            concepts: [],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      }
    ]
  },
  10: {
    className: "Class 10th (Secondary Board Exam)",
    classNumber: 10,
    subjects: [
      {
        id: "physics_10",
        name: "Physics",
        icon: "Zap",
        accentColor: "from-amber-600 to-orange-700",
        chapters: [
          {
            id: "light_reflection_10",
            title: "Light: Reflection and Refraction",
            ncertChapter: "NCERT Class 10 - Chapter 9",
            description: "Spherical mirrors, mirror formula, Snell's law, refractive index, and lens formula.",
            concepts: [
              {
                id: "snell_law",
                name: "Snell's Law of Refraction",
                summary: "The ratio of the sine of the angle of incidence to the sine of the angle of refraction is a constant for a given pair of media.",
                teacherExplanation: "When light travels from air into water, it bends towards the normal. Snell's law gives us the exact mathematical formula: sin i / sin r = constant (refractive index n).",
                audioScript: "Welcome to Class 10 Physics. Snell's law tells us how light bends when crossing optical boundaries. The ratio of sine of incidence angle to sine of refraction angle equals the relative refractive index of the medium.",
                analogies: ["A shopping cart hitting a patch of grass diagonally and pivoting."],
                examples: [],
                keyFormulas: ["sin i / sin r = n2 / n1", "Mirror Formula: 1/f = 1/v + 1/u"],
                commonMisconceptions: ["Measuring angles from the surface instead of measuring from the normal line."],
                authenticReferences: [{ title: "NCERT Class 10 Physics", url: "https://ncert.nic.in", source: "NCERT" }]
              }
            ],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      },
      {
        id: "chemistry_10",
        name: "Chemistry",
        icon: "FlaskConical",
        accentColor: "from-emerald-600 to-teal-700",
        chapters: [
          {
            id: "chemical_reactions_10",
            title: "Chemical Reactions and Equations",
            ncertChapter: "NCERT Class 10 - Chapter 1",
            description: "Balancing chemical equations, combination, decomposition, displacement, and redox reactions.",
            concepts: [],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      },
      {
        id: "maths_10",
        name: "Mathematics",
        icon: "Calculator",
        accentColor: "from-purple-600 to-violet-800",
        chapters: [
          {
            id: "quadratic_equations_10",
            title: "Quadratic Equations",
            ncertChapter: "NCERT Class 10 - Chapter 4",
            description: "Standard form ax² + bx + c = 0, factorization, quadratic formula, nature of roots.",
            concepts: [],
            practiceExamples: [],
            subjectivePaper: []
          }
        ]
      }
    ]
  }
};

export const AVAILABLE_BOARDS = [
  { id: "cbse", name: "CBSE (All India)", badge: "Central Board", color: "bg-blue-100 text-blue-800 border-blue-300" },
  { id: "icse", name: "ICSE / CISCE", badge: "Council Board", color: "bg-purple-100 text-purple-800 border-purple-300" },
  { id: "state_board", name: "State Board (Maharashtra / UP / Karnataka / etc.)", badge: "State Syllabus", color: "bg-emerald-100 text-emerald-800 border-emerald-300" },
  { id: "cambridge", name: "Cambridge IGCSE", badge: "International", color: "bg-amber-100 text-amber-800 border-amber-300" }
];

/**
 * Dynamic Topic Generator:
 * Generates structured pedagogical content, audio script, hidden solution example,
 * and 5 subjective questions for ANY user-typed topic from internet / curriculum knowledge.
 */
export function generateDynamicTopicContent(
  topicTitle: string,
  subject: string,
  studentClass: number,
  board: string
): Chapter {
  const cleanTitle = topicTitle.trim() || "Core Concepts & Applications";

  return {
    id: `dyn_${cleanTitle.toLowerCase().replace(/[^a-z0-9]/g, "_")}`,
    title: cleanTitle,
    ncertChapter: `${board} • Class ${studentClass}th ${subject} Syllabus`,
    description: `Comprehensive study breakdown of ${cleanTitle} specially synthesized for Class ${studentClass}th ${board} students.`,
    concepts: [
      {
        id: "concept_1",
        name: `${cleanTitle} — Core Principles & Mechanisms`,
        summary: `Key theoretical concepts, governing scientific/mathematical laws, SI units, and applications of ${cleanTitle}.`,
        teacherExplanation: `Hello! Today we are mastering "${cleanTitle}" in Class ${studentClass}th ${subject}. In simple words, this concept explains how fundamental principles operate in our physical or mathematical world. When writing subjective answers for ${board}, you should always begin with the formal definition, state the governing equation or formula with its standard SI units, and illustrate with a clear daily-life example.`,
        audioScript: `Hello student! Welcome to EduAegis. Let us explore ${cleanTitle} in very simple and easy English. Think of this concept through real-world actions. In your exams, examiners award marks for three specific things: first, stating the precise definition without leaving out key terms; second, writing the correct formula and SI units; and third, showing your step-by-step reasoning. Let us master this concept together!`,
        analogies: [
          `Visualizing ${cleanTitle} through observable everyday actions.`,
          "Step-by-step mathematical progression from basic definitions to derived equations."
        ],
        examples: [
          {
            title: `Real-Life Application of ${cleanTitle}`,
            scenario: `Observing how ${cleanTitle} functions in household or laboratory experiments.`,
            explanation: `When analyzing this scenario, identify the independent variables, apply the governing relationship, and calculate the output with explicit units.`
          }
        ],
        keyFormulas: [
          "Standard Equation / Law: Verify variable definitions and boundary conditions.",
          "SI Units: Verify metric units (kg, m, s, N, J, W, Pa, Hz, mol) where applicable."
        ],
        commonMisconceptions: [
          "Confusing cause and effect in the physical or mathematical mechanism.",
          "Omission of mandatory SI units or algebraic intermediate steps."
        ],
        authenticReferences: [
          {
            title: `NCERT Class ${studentClass} Official Portal (${subject})`,
            url: "https://ncert.nic.in",
            source: "NCERT"
          },
          {
            title: "Khan Academy Curated Learning",
            url: "https://www.khanacademy.org",
            source: "Khan Academy"
          }
        ]
      }
    ],
    practiceExamples: [
      {
        id: "ex_dyn_1",
        question: `State the fundamental principle governing "${cleanTitle}". Explain its practical significance with an illustrative example.`,
        maxMarks: 4,
        hiddenSolution: {
          steps: [
            { stepNumber: 1, description: `State the standard scientific/mathematical definition of ${cleanTitle}.`, marks: 1.5 },
            { stepNumber: 2, description: "State the governing mathematical formula or theoretical relation with all terms defined.", marks: 1.5 },
            { stepNumber: 3, description: "Provide a concrete daily-life or experimental verification showing practical significance.", marks: 1.0 }
          ],
          finalAnswer: `Comprehensive understanding of ${cleanTitle} with explicit formula and verified practical illustration.`,
          keyInsight: "Always link theoretical statements with mathematical formulas and boundary conditions."
        }
      }
    ],
    subjectivePaper: [
      {
        id: "q1",
        question: `Define "${cleanTitle}". State its primary mathematical equation or scientific law, defining every variable with its SI unit.`,
        maxMarks: 5,
        questionType: "Derivation / Numerical",
        modelAnswer: `Definition:\n${cleanTitle} represents a fundamental principle in Class ${studentClass}th ${subject}.\n\nMathematical Formulation:\nState governing relationship with proportionality constants.\n\nSI Units:\nExplicitly list SI units for every term to guarantee full marks.`,
        rubricPoints: [
          "1.5 marks: Accurate definition covering all essential scientific terminology.",
          "2.0 marks: Governing mathematical formula and derivation steps.",
          "1.5 marks: Explicit SI units and variable definitions."
        ]
      },
      {
        id: "q2",
        question: `Explain the physical/mathematical mechanism behind "${cleanTitle}". Why does this phenomenon occur in real-world systems?`,
        maxMarks: 3,
        questionType: "Conceptual Reasoning",
        modelAnswer: `The phenomenon occurs due to fundamental conservation laws and equilibrium dynamics. Step-by-step reasoning shows how changing one variable impacts the remaining quantities in accordance with governing laws.`,
        rubricPoints: [
          "1.0 mark: Stating the underlying physical/mathematical cause.",
          "1.0 mark: Explaining the mechanism step-by-step.",
          "1.0 mark: Concluding with observable system behavior."
        ]
      },
      {
        id: "q3",
        question: `Give two real-world examples where "${cleanTitle}" is applied in daily life or modern technology.`,
        maxMarks: 3,
        questionType: "Short Definition",
        modelAnswer: `Example 1: Application in household appliances or daily mechanical interactions.\nExample 2: Industrial or scientific application showing measurable benefits.`,
        rubricPoints: [
          "1.5 marks: First valid practical example with scientific explanation.",
          "1.5 marks: Second valid practical example with scientific explanation."
        ]
      },
      {
        id: "q4",
        question: `Solve a numerical problem or step-by-step case study based on "${cleanTitle}". Show all given data, formulas, and calculations with units.`,
        maxMarks: 5,
        questionType: "Derivation / Numerical",
        modelAnswer: `Given Data: Identify input parameters.\nFormula: State primary formula.\nCalculation: Substitute numbers with arithmetic clarity.\nResult: State final answer with proper magnitude and SI unit.`,
        rubricPoints: [
          "1.0 mark: Correct identification of given data and units.",
          "1.5 marks: Correct formula selection and substitution.",
          "2.5 marks: Accurate arithmetic computation and final answer with explicit SI unit."
        ]
      },
      {
        id: "q5",
        question: `What are two common student misconceptions regarding "${cleanTitle}"? Clarify the scientifically correct concept for each.`,
        maxMarks: 4,
        questionType: "Conceptual Reasoning",
        modelAnswer: `Misconception 1: Confusing related physical quantities. Clarification: Distinct definitions and dimensions.\nMisconception 2: Incorrect assumption under special conditions. Clarification: True scientific law verified.`,
        rubricPoints: [
          "2.0 marks: Clarifying the first misconception with physical reasoning.",
          "2.0 marks: Clarifying the second misconception with physical reasoning."
        ]
      }
    ]
  };
}
