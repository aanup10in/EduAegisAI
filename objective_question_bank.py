"""
Objective Question Bank (MCQs) for EduAegis
Covers Classes 8th, 9th, and 10th across Physics, Chemistry, and Mathematics.
Each set contains exactly 5 multiple choice questions with 4 options (A, B, C, D),
radio button options, 1 mark each, correct answers, and conceptual explanations.
"""

def get_full_objective_bank():
    ob = {}

    # =========================================================================
    # CLASS 8
    # =========================================================================
    # Class 8 Physics
    ob[(8, "Physics")] = [
        {
            "topic": "Force & Pressure (Fundamentals & Atmospheric)",
            "questions": [
                {
                    "id": "mcq_8_p1_1",
                    "question": "What is the SI unit of pressure?",
                    "options": [
                        "A. Newton (N)",
                        "B. Pascal (Pa)",
                        "C. Joule (J)",
                        "D. Watt (W)"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Pascal (Pa)",
                    "explanation": "Pressure is force per unit area (P = F / A). Its SI unit is Newton per square meter (N/m²), which is named Pascal (Pa)."
                },
                {
                    "id": "mcq_8_p1_2",
                    "question": "Which of the following is an example of a non-contact force?",
                    "options": [
                        "A. Muscular force",
                        "B. Frictional force",
                        "C. Gravitational force",
                        "D. Mechanical force"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Gravitational force",
                    "explanation": "Gravitational force acts across distance without any physical contact between masses, making it a non-contact force."
                },
                {
                    "id": "mcq_8_p1_3",
                    "question": "As we go higher up a mountain, atmospheric pressure:",
                    "options": [
                        "A. Decreases",
                        "B. Increases",
                        "C. Remains unchanged",
                        "D. First increases then decreases"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Decreases",
                    "explanation": "Atmospheric pressure decreases with altitude because the column and density of air above us decrease."
                },
                {
                    "id": "mcq_8_p1_4",
                    "question": "A force of 100 N acts on an area of 2 m². What is the pressure produced?",
                    "options": [
                        "A. 200 Pa",
                        "B. 50 Pa",
                        "C. 0.02 Pa",
                        "D. 25 Pa"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 50 Pa",
                    "explanation": "Pressure P = Force / Area = 100 N / 2 m² = 50 Pascals (Pa)."
                },
                {
                    "id": "mcq_8_p1_5",
                    "question": "Which instrument is specifically used to measure liquid pressure at a given depth?",
                    "options": [
                        "A. Barometer",
                        "B. Manometer",
                        "C. Thermometer",
                        "D. Hydrometer"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Manometer",
                    "explanation": "A manometer (U-tube manometer) is used to measure liquid pressure differences, while a barometer measures atmospheric pressure."
                }
            ]
        },
        {
            "topic": "Friction & Streamlining (Static, Sliding & Rolling)",
            "questions": [
                {
                    "id": "mcq_8_p2_1",
                    "question": "Which type of friction has the maximum value among the following?",
                    "options": [
                        "A. Rolling friction",
                        "B. Sliding friction",
                        "C. Static friction (limiting)",
                        "D. Fluid drag"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Static friction (limiting)",
                    "explanation": "Limiting static friction is greater than sliding friction, which in turn is much greater than rolling friction (Static > Sliding > Rolling)."
                },
                {
                    "id": "mcq_8_p2_2",
                    "question": "Why are vehicle tyres provided with deep treads and grooves?",
                    "options": [
                        "A. To look visually attractive",
                        "B. To increase friction for better road grip",
                        "C. To decrease vehicle weight",
                        "D. To reduce rolling friction to zero"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. To increase friction for better road grip",
                    "explanation": "Treads increase the roughness of the tyre surface, increasing friction to prevent skidding and provide road grip."
                },
                {
                    "id": "mcq_8_p2_3",
                    "question": "The frictional force exerted by fluids (liquids and gases) is commonly termed as:",
                    "options": [
                        "A. Drag",
                        "B. Thrust",
                        "C. Buoyancy",
                        "D. Tension"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Drag",
                    "explanation": "Fluid friction opposing the motion of objects moving through air or water is called drag."
                },
                {
                    "id": "mcq_8_p2_4",
                    "question": "Substances like oil, grease, or graphite that are applied to reduce friction are called:",
                    "options": [
                        "A. Catalysts",
                        "B. Lubricants",
                        "C. Insulators",
                        "D. Polymers"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Lubricants",
                    "explanation": "Lubricants form a thin slippery layer between interlocking irregularities of surfaces, dramatically reducing friction."
                },
                {
                    "id": "mcq_8_p2_5",
                    "question": "Why do aeroplanes and high-speed trains have streamlined shapes?",
                    "options": [
                        "A. To reduce fluid friction (air drag)",
                        "B. To increase gravitational attraction",
                        "C. To increase air resistance",
                        "D. To make manufacturing cheaper"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. To reduce fluid friction (air drag)",
                    "explanation": "Streamlined body shapes allow fluid layers to flow smoothly around the vehicle, minimizing drag and saving fuel."
                }
            ]
        },
        {
            "topic": "Sound & Vibration (Frequency, Pitch & Loudness)",
            "questions": [
                {
                    "id": "mcq_8_p3_1",
                    "question": "Sound waves cannot propagate through which of the following media?",
                    "options": [
                        "A. Water",
                        "B. Steel rod",
                        "C. Vacuum",
                        "D. Nitrogen gas"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Vacuum",
                    "explanation": "Sound is a mechanical wave requiring a material medium (solid, liquid, or gas) to propagate. It cannot travel in a vacuum."
                },
                {
                    "id": "mcq_8_p3_2",
                    "question": "The pitch or shrillness of a sound is directly determined by its:",
                    "options": [
                        "A. Amplitude",
                        "B. Frequency",
                        "C. Speed",
                        "D. Timbre"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Frequency",
                    "explanation": "Frequency determines the pitch or shrillness of sound. Higher frequency means higher pitch."
                },
                {
                    "id": "mcq_8_p3_3",
                    "question": "The audible range of sound frequencies for a normal human ear is:",
                    "options": [
                        "A. 2 Hz to 2,000 Hz",
                        "B. 20 Hz to 20,000 Hz",
                        "C. 200 Hz to 200,000 Hz",
                        "D. 0 Hz to 100 Hz"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 20 Hz to 20,000 Hz",
                    "explanation": "Humans can hear frequencies between 20 Hz (infrasonic threshold) and 20,000 Hz / 20 kHz (ultrasonic threshold)."
                },
                {
                    "id": "mcq_8_p3_4",
                    "question": "The loudness of sound is directly proportional to the square of its:",
                    "options": [
                        "A. Frequency",
                        "B. Time period",
                        "C. Amplitude of vibration",
                        "D. Wavelength"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Amplitude of vibration",
                    "explanation": "Loudness is proportional to the square of the amplitude of vibration (Loudness ∝ Amplitude²)."
                },
                {
                    "id": "mcq_8_p3_5",
                    "question": "The number of complete oscillations per second made by a vibrating body is called its:",
                    "options": [
                        "A. Wavelength",
                        "B. Frequency",
                        "C. Time period",
                        "D. Amplitude"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Frequency",
                    "explanation": "Frequency is defined as the number of oscillations per second and is measured in Hertz (Hz)."
                }
            ]
        }
    ]

    # Class 8 Chemistry
    ob[(8, "Chemistry")] = [
        {
            "topic": "Synthetic Fibres & Plastics (Polymers)",
            "questions": [
                {
                    "id": "mcq_8_c1_1",
                    "question": "Which was the first fully synthetic fibre produced without any natural raw material?",
                    "options": [
                        "A. Rayon",
                        "B. Nylon",
                        "C. Polyester",
                        "D. Acrylic"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Nylon",
                    "explanation": "Nylon, synthesized in 1931 from coal, water, and air without plant or animal raw materials, was the first fully synthetic fibre."
                },
                {
                    "id": "mcq_8_c1_2",
                    "question": "Rayon is prepared from wood pulp and is commonly referred to as:",
                    "options": [
                        "A. Artificial wool",
                        "B. Artificial silk",
                        "C. Plastic wool",
                        "D. Pure cellulose"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Artificial silk",
                    "explanation": "Rayon resembles pure silk in texture and sheen, so it is commercially known as artificial silk."
                },
                {
                    "id": "mcq_8_c1_3",
                    "question": "Which of the following is a thermosetting plastic used in electrical switches?",
                    "options": [
                        "A. Polythene",
                        "B. PVC",
                        "C. Bakelite",
                        "D. Polystyrene"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Bakelite",
                    "explanation": "Bakelite is a poor conductor of heat and electricity and does not soften on reheating, making it ideal for electrical switches."
                },
                {
                    "id": "mcq_8_c1_4",
                    "question": "The monomer building block of the natural polymer cellulose is:",
                    "options": [
                        "A. Amino acid",
                        "B. Glucose",
                        "C. Ethene",
                        "D. Ester"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Glucose",
                    "explanation": "Cellulose is a polysaccharide polymer composed of repeating glucose units joined by glycosidic bonds."
                },
                {
                    "id": "mcq_8_c1_5",
                    "question": "Plastics that can be repeatedly softened by heating and remoulded are called:",
                    "options": [
                        "A. Thermoplastics",
                        "B. Thermosetting plastics",
                        "C. Natural resins",
                        "D. Melamines"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Thermoplastics",
                    "explanation": "Thermoplastics (like Polythene and PVC) soften easily when heated and can be bent and recycled."
                }
            ]
        },
        {
            "topic": "Metals & Non-Metals (Reactivity & Physical Properties)",
            "questions": [
                {
                    "id": "mcq_8_c2_1",
                    "question": "Which metal is found in liquid state at room temperature?",
                    "options": [
                        "A. Sodium",
                        "B. Mercury",
                        "C. Aluminium",
                        "D. Lead"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Mercury",
                    "explanation": "Mercury (Hg) is the only metal that is liquid at standard room temperature (25°C)."
                },
                {
                    "id": "mcq_8_c2_2",
                    "question": "Which non-metal is an exceptionally good conductor of electricity?",
                    "options": [
                        "A. Sulphur",
                        "B. Phosphorus",
                        "C. Graphite",
                        "D. Diamond"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Graphite",
                    "explanation": "Graphite (an allotrope of carbon) has delocalized free electrons between hexagonal layers, conducting electricity."
                },
                {
                    "id": "mcq_8_c2_3",
                    "question": "What gas is liberated when zinc reacts with dilute hydrochloric acid?",
                    "options": [
                        "A. Oxygen",
                        "B. Hydrogen",
                        "C. Chlorine",
                        "D. Carbon dioxide"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Hydrogen",
                    "explanation": "Zn + 2HCl → ZnCl₂ + H₂↑. Hydrogen gas burns with a characteristic 'pop' sound."
                },
                {
                    "id": "mcq_8_c2_4",
                    "question": "The property of metals that allows them to be drawn into thin wires is:",
                    "options": [
                        "A. Malleability",
                        "B. Ductility",
                        "C. Sonority",
                        "D. Lustre"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Ductility",
                    "explanation": "Ductility is the property by which metals can be drawn into thin wires without breaking (Gold is the most ductile)."
                },
                {
                    "id": "mcq_8_c2_5",
                    "question": "Which of the following is the most reactive metal in the reactivity series?",
                    "options": [
                        "A. Iron (Fe)",
                        "B. Copper (Cu)",
                        "C. Potassium (K)",
                        "D. Zinc (Zn)"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Potassium (K)",
                    "explanation": "Potassium (K) is at the top of the metal reactivity series and reacts vigorously even with cold water."
                }
            ]
        },
        {
            "topic": "Combustion & Flame (Calorific Value & Fire Control)",
            "questions": [
                {
                    "id": "mcq_8_c3_1",
                    "question": "Which zone of a candle flame is the hottest?",
                    "options": [
                        "A. Innermost dark zone",
                        "B. Middle luminous yellow zone",
                        "C. Outermost non-luminous blue zone",
                        "D. Wick zone"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Outermost non-luminous blue zone",
                    "explanation": "The outermost zone receives plentiful oxygen for complete combustion, making it the hottest part of the flame (used by goldsmiths)."
                },
                {
                    "id": "mcq_8_c3_2",
                    "question": "The lowest temperature at which a substance catches fire is called its:",
                    "options": [
                        "A. Boiling point",
                        "B. Melting point",
                        "C. Ignition temperature",
                        "D. Critical temperature"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Ignition temperature",
                    "explanation": "Ignition temperature is the minimum temperature required for a combustible substance to ignite and sustain combustion."
                },
                {
                    "id": "mcq_8_c3_3",
                    "question": "The calorific value of a fuel is expressed in which standard unit?",
                    "options": [
                        "A. kJ/kg",
                        "B. kg/kJ",
                        "C. Joules/second",
                        "D. Calories/gram"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. kJ/kg",
                    "explanation": "Calorific value is the amount of heat energy released on complete combustion of 1 kg of fuel, measured in kJ/kg."
                },
                {
                    "id": "mcq_8_c3_4",
                    "question": "Which gas is the best extinguisher for electrical equipment fires?",
                    "options": [
                        "A. Oxygen",
                        "B. Carbon dioxide (CO₂)",
                        "C. Hydrogen",
                        "D. Chlorine"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Carbon dioxide (CO₂)",
                    "explanation": "CO₂ is non-conductive, heavier than air, and smothers the fire by cutting off the oxygen supply without damaging electrical circuits."
                },
                {
                    "id": "mcq_8_c3_5",
                    "question": "Incomplete combustion of fuels produces which poisonous gas that binds strongly to haemoglobin?",
                    "options": [
                        "A. Carbon dioxide",
                        "B. Carbon monoxide",
                        "C. Sulphur dioxide",
                        "D. Nitrogen dioxide"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Carbon monoxide",
                    "explanation": "Carbon monoxide (CO) is a silent, toxic gas produced by incomplete combustion that forms carboxyhaemoglobin in blood."
                }
            ]
        }
    ]

    # Class 8 Mathematics
    ob[(8, "Mathematics")] = [
        {
            "topic": "Rational Numbers (Properties & Identities)",
            "questions": [
                {
                    "id": "mcq_8_m1_1",
                    "question": "What is the additive identity element for rational numbers?",
                    "options": [
                        "A. 1",
                        "B. 0",
                        "C. -1",
                        "D. Any integer"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 0",
                    "explanation": "Adding 0 to any rational number a/b yields a/b (a/b + 0 = a/b), so 0 is the additive identity."
                },
                {
                    "id": "mcq_8_m1_2",
                    "question": "What is the multiplicative inverse (reciprocal) of -5/8?",
                    "options": [
                        "A. 5/8",
                        "B. -8/5",
                        "C. 8/5",
                        "D. -1"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -8/5",
                    "explanation": "The multiplicative inverse of a rational number p/q is q/p such that (p/q) × (q/p) = 1. Reciprocal of -5/8 is -8/5."
                },
                {
                    "id": "mcq_8_m1_3",
                    "question": "How many rational numbers exist between any two distinct rational numbers?",
                    "options": [
                        "A. Exactly 10",
                        "B. Exactly 100",
                        "C. Infinitely many",
                        "D. Zero"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Infinitely many",
                    "explanation": "Between any two distinct rational numbers, there are infinitely many rational numbers (density property of rationals)."
                },
                {
                    "id": "mcq_8_m1_4",
                    "question": "Which rational number has no reciprocal?",
                    "options": [
                        "A. 1",
                        "B. -1",
                        "C. 0",
                        "D. 1/2"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 0",
                    "explanation": "Division by zero is undefined, so 0 does not have a multiplicative inverse (reciprocal)."
                },
                {
                    "id": "mcq_8_m1_5",
                    "question": "What is the result of (-3/7) + (2/7)?",
                    "options": [
                        "A. 5/7",
                        "B. -1/7",
                        "C. -5/7",
                        "D. 1/7"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -1/7",
                    "explanation": "Common denominator is 7: (-3 + 2) / 7 = -1/7."
                }
            ]
        },
        {
            "topic": "Linear Equations in One Variable (Algebraic Solutions)",
            "questions": [
                {
                    "id": "mcq_8_m2_1",
                    "question": "Solve for x: 3x - 5 = 10.",
                    "options": [
                        "A. x = 3",
                        "B. x = 5",
                        "C. x = 15",
                        "D. x = 5/3"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. x = 5",
                    "explanation": "3x = 10 + 5 => 3x = 15 => x = 15 / 3 = 5."
                },
                {
                    "id": "mcq_8_m2_2",
                    "question": "What is the highest power (degree) of the variable in a linear equation?",
                    "options": [
                        "A. 0",
                        "B. 1",
                        "C. 2",
                        "D. Any power"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 1",
                    "explanation": "By definition, a linear equation has degree 1, meaning the variable's highest exponent is 1."
                },
                {
                    "id": "mcq_8_m2_3",
                    "question": "If 2y + 9 = 4, then y equals:",
                    "options": [
                        "A. 5/2",
                        "B. -5/2",
                        "C. -13/2",
                        "D. 13/2"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -5/2",
                    "explanation": "2y = 4 - 9 => 2y = -5 => y = -5/2."
                },
                {
                    "id": "mcq_8_m2_4",
                    "question": "The sum of three consecutive integers is 51. The middle integer is:",
                    "options": [
                        "A. 16",
                        "B. 17",
                        "C. 18",
                        "D. 15"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 17",
                    "explanation": "Let integers be (x-1), x, (x+1). Sum = 3x = 51 => x = 17."
                },
                {
                    "id": "mcq_8_m2_5",
                    "question": "Solve for z: (z / 3) + 1 = 7/15.",
                    "options": [
                        "A. z = -8/5",
                        "B. z = 8/5",
                        "C. z = -2/5",
                        "D. z = 22/5"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. z = -8/5",
                    "explanation": "z / 3 = 7/15 - 1 = -8/15 => z = 3 × (-8/15) = -8/5."
                }
            ]
        },
        {
            "topic": "Understanding Quadrilaterals (Angles & Polygons)",
            "questions": [
                {
                    "id": "mcq_8_m3_1",
                    "question": "What is the sum of all interior angles of a quadrilateral?",
                    "options": [
                        "A. 180°",
                        "B. 360°",
                        "C. 540°",
                        "D. 720°"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 360°",
                    "explanation": "Formula: (n - 2) × 180° for n = 4 gives (4 - 2) × 180° = 360°."
                },
                {
                    "id": "mcq_8_m3_2",
                    "question": "What is the sum of exterior angles of any convex polygon regardless of number of sides?",
                    "options": [
                        "A. 180°",
                        "B. 360°",
                        "C. 540°",
                        "D. Depends on number of sides"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 360°",
                    "explanation": "For any convex polygon, the sum of exterior angles taken in order is always equal to 360° (4 right angles)."
                },
                {
                    "id": "mcq_8_m3_3",
                    "question": "The diagonals of a rhombus intersect each other at an angle of:",
                    "options": [
                        "A. 45°",
                        "B. 60°",
                        "C. 90° (right angle)",
                        "D. 120°"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 90° (right angle)",
                    "explanation": "A defining property of a rhombus is that its diagonals bisect each other perpendicularly at 90°."
                },
                {
                    "id": "mcq_8_m3_4",
                    "question": "How many diagonals does a regular hexagon (6 sides) possess?",
                    "options": [
                        "A. 6",
                        "B. 9",
                        "C. 12",
                        "D. 15"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 9",
                    "explanation": "Formula for number of diagonals in an n-gon is n(n - 3) / 2. For n = 6: 6 × 3 / 2 = 9 diagonals."
                },
                {
                    "id": "mcq_8_m3_5",
                    "question": "A parallelogram whose adjacent sides are equal and all angles are 90° is a:",
                    "options": [
                        "A. Rectangle",
                        "B. Rhombus",
                        "C. Square",
                        "D. Trapezium"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Square",
                    "explanation": "Equal adjacent sides and right angles define a square."
                }
            ]
        }
    ]

    # =========================================================================
    # CLASS 9
    # =========================================================================
    # Class 9 Physics
    ob[(9, "Physics")] = [
        {
            "topic": "Motion (Kinematics, Graphs & Equations)",
            "questions": [
                {
                    "id": "mcq_9_p1_1",
                    "question": "What is the SI unit of acceleration?",
                    "options": [
                        "A. m/s",
                        "B. m/s²",
                        "C. km/h",
                        "D. N/kg·m"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. m/s²",
                    "explanation": "Acceleration is rate of change of velocity ((m/s) / s), so its SI unit is meter per second squared (m/s²)."
                },
                {
                    "id": "mcq_9_p1_2",
                    "question": "The area under a velocity-time (v-t) graph represents:",
                    "options": [
                        "A. Acceleration",
                        "B. Displacement",
                        "C. Force",
                        "D. Speed only"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Displacement",
                    "explanation": "Area under v-t graph = velocity × time, which has units of distance/displacement."
                },
                {
                    "id": "mcq_9_p1_3",
                    "question": "A car accelerates uniformly from rest at 2 m/s² for 5 seconds. How much distance does it cover?",
                    "options": [
                        "A. 10 m",
                        "B. 25 m",
                        "C. 50 m",
                        "D. 20 m"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 25 m",
                    "explanation": "Using s = ut + 0.5at²: With u = 0, s = 0.5 × 2 × (5)² = 25 meters."
                },
                {
                    "id": "mcq_9_p1_4",
                    "question": "The slope of a distance-time graph indicates:",
                    "options": [
                        "A. Acceleration",
                        "B. Speed",
                        "C. Momentum",
                        "D. Displacement"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Speed",
                    "explanation": "Slope = Δdistance / Δtime = Speed of the object."
                },
                {
                    "id": "mcq_9_p1_5",
                    "question": "In uniform circular motion, which quantity remains constant?",
                    "options": [
                        "A. Velocity",
                        "B. Acceleration direction",
                        "C. Speed",
                        "D. Displacement"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Speed",
                    "explanation": "In uniform circular motion, speed is constant while direction of velocity changes continuously, causing centripetal acceleration."
                }
            ]
        },
        {
            "topic": "Force & Laws of Motion (Inertia & Momentum)",
            "questions": [
                {
                    "id": "mcq_9_p2_1",
                    "question": "The inertia of an object is directly proportional to its:",
                    "options": [
                        "A. Velocity",
                        "B. Volume",
                        "C. Mass",
                        "D. Weight"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Mass",
                    "explanation": "Mass is the quantitative measure of inertia. Greater mass means greater inertia."
                },
                {
                    "id": "mcq_9_p2_2",
                    "question": "Newton's Second Law of Motion provides a quantitative formula for force:",
                    "options": [
                        "A. F = m / a",
                        "B. F = m × a",
                        "C. F = v / t",
                        "D. F = 0.5 m v²"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. F = m × a",
                    "explanation": "Force equals rate of change of momentum: F = d(mv)/dt = m × a (when mass is constant)."
                },
                {
                    "id": "mcq_9_p2_3",
                    "question": "What is the SI unit of linear momentum (p = mv)?",
                    "options": [
                        "A. kg·m/s²",
                        "B. kg·m/s",
                        "C. N·m",
                        "D. J·s"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. kg·m/s",
                    "explanation": "Momentum = mass (kg) × velocity (m/s) = kg·m/s (or N·s)."
                },
                {
                    "id": "mcq_9_p2_4",
                    "question": "According to Newton's Third Law, action and reaction forces act:",
                    "options": [
                        "A. On the same body in the same direction",
                        "B. On two different bodies in opposite directions",
                        "C. On the same body in opposite directions",
                        "D. At different times"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. On two different bodies in opposite directions",
                    "explanation": "Action and reaction are always equal and opposite, acting simultaneously on two different interacting bodies."
                },
                {
                    "id": "mcq_9_p2_5",
                    "question": "The recoil of a rifle when a bullet is fired is an example of:",
                    "options": [
                        "A. Conservation of energy",
                        "B. Conservation of linear momentum",
                        "C. Conservation of charge",
                        "D. Archimedes' principle"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Conservation of linear momentum",
                    "explanation": "Total momentum before firing is zero; forward momentum of bullet equals backward recoil momentum of rifle."
                }
            ]
        },
        {
            "topic": "Gravitation & Floatation (Universal Law & Buoyancy)",
            "questions": [
                {
                    "id": "mcq_9_p3_1",
                    "question": "The value of the Universal Gravitational Constant G is:",
                    "options": [
                        "A. 9.8 m/s²",
                        "B. 6.673 × 10⁻¹¹ N·m²/kg²",
                        "C. 6.673 × 10¹¹ N·m²/kg²",
                        "D. 9.8 × 10⁻¹¹ N·m²/kg²"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 6.673 × 10⁻¹¹ N·m²/kg²",
                    "explanation": "Sir Henry Cavendish measured G = 6.673 × 10⁻¹¹ N·m²/kg²."
                },
                {
                    "id": "mcq_9_p3_2",
                    "question": "The weight of an object on the Moon is approximately what fraction of its weight on Earth?",
                    "options": [
                        "A. 1/2",
                        "B. 1/4",
                        "C. 1/6",
                        "D. 1/10"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 1/6",
                    "explanation": "Surface gravity on the Moon (g_moon) is about 1/6th of g_earth (1.63 m/s² vs 9.8 m/s²)."
                },
                {
                    "id": "mcq_9_p3_3",
                    "question": "What is the value of acceleration due to gravity 'g' at the centre of the Earth?",
                    "options": [
                        "A. 9.8 m/s²",
                        "B. Infinity",
                        "C. 0 m/s²",
                        "D. 4.9 m/s²"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 0 m/s²",
                    "explanation": "At the geometric centre of the Earth, gravitational pulls from all surrounding spherical shells cancel out, making g = 0."
                },
                {
                    "id": "mcq_9_p3_4",
                    "question": "According to Archimedes' Principle, the upward buoyant force on an immersed body equals:",
                    "options": [
                        "A. Volume of the body",
                        "B. Weight of the fluid displaced by the body",
                        "C. Total weight of the liquid container",
                        "D. Atmospheric pressure"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Weight of the fluid displaced by the body",
                    "explanation": "Archimedes' Principle states that buoyant force equals the weight of the fluid displaced."
                },
                {
                    "id": "mcq_9_p3_5",
                    "question": "An iron nail sinks in water while a massive steel ship floats because:",
                    "options": [
                        "A. Steel is lighter than water",
                        "B. The ship's hollow hull displaces a volume of water whose weight exceeds the ship's total weight",
                        "C. Sea water has zero surface tension",
                        "D. Iron reacts with water"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. The ship's hollow hull displaces a volume of water whose weight exceeds the ship's total weight",
                    "explanation": "The ship's hollow shape gives it an average density lower than water, displacing enough water weight to balance its mass."
                }
            ]
        }
    ]

    # Class 9 Chemistry
    ob[(9, "Chemistry")] = [
        {
            "topic": "Matter in Our Surroundings (States & Evaporation)",
            "questions": [
                {
                    "id": "mcq_9_c1_1",
                    "question": "What is the SI unit of temperature?",
                    "options": [
                        "A. Degree Celsius (°C)",
                        "B. Kelvin (K)",
                        "C. Fahrenheit (°F)",
                        "D. Joule (J)"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Kelvin (K)",
                    "explanation": "Kelvin (K) is the SI base unit of thermodynamic temperature (0°C = 273.15 K)."
                },
                {
                    "id": "mcq_9_c1_2",
                    "question": "The phase change directly from solid to gas without entering the liquid state is called:",
                    "options": [
                        "A. Vaporization",
                        "B. Sublimation",
                        "C. Condensation",
                        "D. Fusion"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Sublimation",
                    "explanation": "Sublimation is the direct transition of a substance from solid to gas (e.g. camphor, dry ice, ammonium chloride)."
                },
                {
                    "id": "mcq_9_c1_3",
                    "question": "Which of the following factors causes a decrease in the rate of evaporation of water?",
                    "options": [
                        "A. Increase in surface area",
                        "B. Increase in temperature",
                        "C. Increase in humidity",
                        "D. Increase in wind speed"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Increase in humidity",
                    "explanation": "High humidity means air already holds substantial water vapour, which impedes further evaporation."
                },
                {
                    "id": "mcq_9_c1_4",
                    "question": "What is 'Dry Ice' chemically?",
                    "options": [
                        "A. Solid nitrogen",
                        "B. Solid carbon dioxide (CO₂)",
                        "C. Solid water at -50°C",
                        "D. Solid methane"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Solid carbon dioxide (CO₂)",
                    "explanation": "Dry ice is solid carbon dioxide under high pressure; when released to 1 atm, it sublimes directly into gas."
                },
                {
                    "id": "mcq_9_c1_5",
                    "question": "During melting of ice at 0°C, temperature remains constant because supplied heat is used as:",
                    "options": [
                        "A. Latent heat of fusion to break intermolecular attractions",
                        "B. Kinetic energy of molecules",
                        "C. Chemical bond energy",
                        "D. Radiation loss"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Latent heat of fusion to break intermolecular attractions",
                    "explanation": "Heat energy supplied during phase change is latent heat of fusion, overcoming intermolecular forces without raising temperature."
                }
            ]
        },
        {
            "topic": "Is Matter Around Us Pure (Mixtures & Colloids)",
            "questions": [
                {
                    "id": "mcq_9_c2_1",
                    "question": "The scattering of a visible beam of light by particles in a colloidal sol is called:",
                    "options": [
                        "A. Raman effect",
                        "B. Tyndall effect",
                        "C. Doppler effect",
                        "D. Zeeman effect"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Tyndall effect",
                    "explanation": "Colloidal particles have dimensions (1-1000 nm) sufficient to scatter light wavelengths, creating the Tyndall effect."
                },
                {
                    "id": "mcq_9_c2_2",
                    "question": "Which of the following is a homogeneous mixture (true solution)?",
                    "options": [
                        "A. Milk",
                        "B. Chalk powder in water",
                        "C. Brass (alloy of copper and zinc)",
                        "D. Muddy pond water"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Brass (alloy of copper and zinc)",
                    "explanation": "Brass is a solid-in-solid homogeneous solution with uniform composition throughout."
                },
                {
                    "id": "mcq_9_c2_3",
                    "question": "Two immiscible liquids like kerosene and water can be separated using:",
                    "options": [
                        "A. Fractional distillation",
                        "B. Separating funnel",
                        "C. Chromatography",
                        "D. Centrifugation"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Separating funnel",
                    "explanation": "A separating funnel utilizes differences in liquid densities to separate immiscible liquid layers."
                },
                {
                    "id": "mcq_9_c2_4",
                    "question": "Which of the following is an example of an aerosol colloid?",
                    "options": [
                        "A. Fog and smoke",
                        "B. Cheese",
                        "C. Shaving cream",
                        "D. Coloured gemstone"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Fog and smoke",
                    "explanation": "An aerosol is a colloid where liquid droplets or solid smoke particles are dispersed in gas medium."
                },
                {
                    "id": "mcq_9_c2_5",
                    "question": "A pure chemical substance has which distinctive characteristic?",
                    "options": [
                        "A. Can be separated by filtration",
                        "B. Has sharp, fixed melting and boiling points",
                        "C. Variable composition",
                        "D. Shows Tyndall effect"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Has sharp, fixed melting and boiling points",
                    "explanation": "Pure substances have fixed chemical compositions and sharp, well-defined melting and boiling points."
                }
            ]
        },
        {
            "topic": "Atoms, Molecules & Mole Concept",
            "questions": [
                {
                    "id": "mcq_9_c3_1",
                    "question": "The numerical value of Avogadro's Constant (N_A) is:",
                    "options": [
                        "A. 6.022 × 10²³ per mole",
                        "B. 6.022 × 10²² per mole",
                        "C. 1.602 × 10⁻¹⁹ per mole",
                        "D. 3.00 × 10⁸ per mole"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. 6.022 × 10²³ per mole",
                    "explanation": "One mole of any substance contains exactly 6.022 × 10²³ elementary entities (Avogadro's number)."
                },
                {
                    "id": "mcq_9_c3_2",
                    "question": "What is the molecular mass of water (H₂O) in unified atomic mass units (u)?",
                    "options": [
                        "A. 16 u",
                        "B. 18 u",
                        "C. 20 u",
                        "D. 32 u"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 18 u",
                    "explanation": "Molecular mass = (2 × 1 u for H) + (1 × 16 u for O) = 18 u."
                },
                {
                    "id": "mcq_9_c3_3",
                    "question": "How many moles are present in 44 grams of carbon dioxide (CO₂)?",
                    "options": [
                        "A. 0.5 mole",
                        "B. 1.0 mole",
                        "C. 2.0 moles",
                        "D. 4.4 moles"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 1.0 mole",
                    "explanation": "Molar mass of CO₂ = 12 + 2(16) = 44 g/mol. Moles = 44 g / 44 g/mol = 1.0 mole."
                },
                {
                    "id": "mcq_9_c3_4",
                    "question": "What is the chemical formula of Aluminium Sulphate?",
                    "options": [
                        "A. AlSO₄",
                        "B. Al₂(SO₄)₃",
                        "C. Al₃(SO₄)₂",
                        "D. Al₂(SO₄)"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Al₂(SO₄)₃",
                    "explanation": "Aluminium valency is +3, sulphate ion is SO₄²⁻. Criss-cross valency yields Al₂(SO₄)₃."
                },
                {
                    "id": "mcq_9_c3_5",
                    "question": "Who formulated the Law of Constant (Definite) Proportions?",
                    "options": [
                        "A. John Dalton",
                        "B. Joseph Proust",
                        "C. Antoine Lavoisier",
                        "D. J.J. Thomson"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Joseph Proust",
                    "explanation": "Joseph Proust stated that in a chemical substance elements are always present in definite proportions by mass."
                }
            ]
        }
    ]

    # Class 9 Mathematics
    ob[(9, "Mathematics")] = [
        {
            "topic": "Number Systems & Real Numbers",
            "questions": [
                {
                    "id": "mcq_9_m1_1",
                    "question": "Which of the following is an irrational number?",
                    "options": [
                        "A. √9",
                        "B. √4",
                        "C. √7",
                        "D. 0.375"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. √7",
                    "explanation": "√7 has a non-terminating, non-recurring decimal expansion and cannot be written as p/q, so it is irrational."
                },
                {
                    "id": "mcq_9_m1_2",
                    "question": "Simplify the algebraic expression: (5 + √5)(5 - √5).",
                    "options": [
                        "A. 20",
                        "B. 30",
                        "C. 25",
                        "D. 10"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. 20",
                    "explanation": "Using identity (a + b)(a - b) = a² - b²: 5² - (√5)² = 25 - 5 = 20."
                },
                {
                    "id": "mcq_9_m1_3",
                    "question": "The decimal expansion of an irrational number is always:",
                    "options": [
                        "A. Terminating",
                        "B. Non-terminating recurring",
                        "C. Non-terminating non-recurring",
                        "D. Repeating integer"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Non-terminating non-recurring",
                    "explanation": "By definition, real numbers with non-terminating and non-recurring decimals are irrational numbers."
                },
                {
                    "id": "mcq_9_m1_4",
                    "question": "Evaluate: (2^(2/3)) × (2^(1/3)).",
                    "options": [
                        "A. 4",
                        "B. 2",
                        "C. 2^(2/9)",
                        "D. 1"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 2",
                    "explanation": "Using a^m × a^n = a^(m+n): 2^(2/3 + 1/3) = 2^(3/3) = 2^1 = 2."
                },
                {
                    "id": "mcq_9_m1_5",
                    "question": "Express 0.6666... (0.6̄) in rational p/q form:",
                    "options": [
                        "A. 6/10",
                        "B. 2/3",
                        "C. 3/2",
                        "D. 6/11"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 2/3",
                    "explanation": "Let x = 0.666... => 10x = 6.666... => 9x = 6 => x = 6/9 = 2/3."
                }
            ]
        },
        {
            "topic": "Polynomials & Factor Theorem",
            "questions": [
                {
                    "id": "mcq_9_m2_1",
                    "question": "What is the degree of the zero polynomial p(x) = 0?",
                    "options": [
                        "A. 0",
                        "B. 1",
                        "C. Not defined",
                        "D. -1"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Not defined",
                    "explanation": "The degree of the zero polynomial is convention-wise not defined."
                },
                {
                    "id": "mcq_9_m2_2",
                    "question": "What is the zero of the polynomial p(x) = 2x + 5?",
                    "options": [
                        "A. 5/2",
                        "B. -5/2",
                        "C. -2/5",
                        "D. 0"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -5/2",
                    "explanation": "Set 2x + 5 = 0 => 2x = -5 => x = -5/2."
                },
                {
                    "id": "mcq_9_m2_3",
                    "question": "If x - 1 is a factor of p(x) = 4x³ + 3x² - 4x + k, find k:",
                    "options": [
                        "A. 3",
                        "B. -3",
                        "C. 4",
                        "D. -4"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -3",
                    "explanation": "By factor theorem, p(1) = 0 => 4(1) + 3(1) - 4(1) + k = 0 => 3 + k = 0 => k = -3."
                },
                {
                    "id": "mcq_9_m2_4",
                    "question": "What is the coefficient of x² in polynomial p(x) = 2 - x² + x³?",
                    "options": [
                        "A. 2",
                        "B. 1",
                        "C. -1",
                        "D. 0"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. -1",
                    "explanation": "The term involving x² is -x² = (-1)x², so the coefficient is -1."
                },
                {
                    "id": "mcq_9_m2_5",
                    "question": "The expanded form of (x + 2y + 4z)² contains how many terms?",
                    "options": [
                        "A. 3",
                        "B. 6",
                        "C. 9",
                        "D. 4"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 6",
                    "explanation": "(a+b+c)² = a² + b² + c² + 2ab + 2bc + 2ca, which has 6 terms."
                }
            ]
        },
        {
            "topic": "Coordinate Geometry & Linear Equations",
            "questions": [
                {
                    "id": "mcq_9_m3_1",
                    "question": "The point (-3, 4) lies in which quadrant of the Cartesian plane?",
                    "options": [
                        "A. Quadrant I",
                        "B. Quadrant II",
                        "C. Quadrant III",
                        "D. Quadrant IV"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Quadrant II",
                    "explanation": "In Quadrant II, x-coordinate is negative and y-coordinate is positive (-x, +y)."
                },
                {
                    "id": "mcq_9_m3_2",
                    "question": "What is the abscissa (x-coordinate) of all points lying on the y-axis?",
                    "options": [
                        "A. 1",
                        "B. 0",
                        "C. -1",
                        "D. Any real number"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 0",
                    "explanation": "Every point on the y-axis has the coordinate form (0, y), so abscissa is identically 0."
                },
                {
                    "id": "mcq_9_m3_3",
                    "question": "The graph of the linear equation y = 3x is a straight line that:",
                    "options": [
                        "A. Passes through the origin (0, 0)",
                        "B. Is parallel to the x-axis",
                        "C. Is parallel to the y-axis",
                        "D. Intersects y-axis at (0, 3)"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. Passes through the origin (0, 0)",
                    "explanation": "When x = 0, y = 3(0) = 0. Hence (0,0) satisfies the equation."
                },
                {
                    "id": "mcq_9_m3_4",
                    "question": "If (2, 0) is a solution of 2x + 3y = k, then k is:",
                    "options": [
                        "A. 2",
                        "B. 4",
                        "C. 6",
                        "D. 0"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 4",
                    "explanation": "Substitute x = 2, y = 0: 2(2) + 3(0) = 4 + 0 = 4 => k = 4."
                },
                {
                    "id": "mcq_9_m3_5",
                    "question": "How many linear equations in x and y can be satisfied by the point (1, 2)?",
                    "options": [
                        "A. Only one",
                        "B. Exactly two",
                        "C. Infinitely many",
                        "D. Zero"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Infinitely many",
                    "explanation": "Through any single point in a plane, infinitely many straight lines can pass."
                }
            ]
        }
    ]

    # =========================================================================
    # CLASS 10
    # =========================================================================
    # Class 10 Physics
    ob[(10, "Physics")] = [
        {
            "topic": "Light - Reflection & Refraction (Optics & Lens Formula)",
            "questions": [
                {
                    "id": "mcq_10_p1_1",
                    "question": "Which type of mirror is used by dentists to view enlarged images of teeth?",
                    "options": [
                        "A. Convex mirror",
                        "B. Concave mirror",
                        "C. Plane mirror",
                        "D. Cylindrical mirror"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Concave mirror",
                    "explanation": "When the object is between pole and focus of a concave mirror, it forms an erect, magnified virtual image."
                },
                {
                    "id": "mcq_10_p1_2",
                    "question": "A convex lens has a optical power of +2.0 D. What is its focal length?",
                    "options": [
                        "A. +50 cm",
                        "B. -50 cm",
                        "C. +20 cm",
                        "D. +100 cm"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. +50 cm",
                    "explanation": "Power P = 1 / f(in meters) => f = 1 / 2.0 = 0.5 m = +50 cm."
                },
                {
                    "id": "mcq_10_p1_3",
                    "question": "If the absolute refractive index of crown glass is 1.5, what is the speed of light in glass? (c = 3 × 10⁸ m/s)",
                    "options": [
                        "A. 1.5 × 10⁸ m/s",
                        "B. 2.0 × 10⁸ m/s",
                        "C. 2.5 × 10⁸ m/s",
                        "D. 3.0 × 10⁸ m/s"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 2.0 × 10⁸ m/s",
                    "explanation": "v = c / n = (3.0 × 10⁸ m/s) / 1.5 = 2.0 × 10⁸ m/s."
                },
                {
                    "id": "mcq_10_p1_4",
                    "question": "The apparent twinkling of stars at night is primarily caused by:",
                    "options": [
                        "A. Atmospheric dispersion",
                        "B. Total internal reflection",
                        "C. Atmospheric refraction through changing air density layers",
                        "D. Gravitational lensing"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Atmospheric refraction through changing air density layers",
                    "explanation": "Varying optical density of atmospheric layers causes continuous fluctuation in the apparent position and intensity of starlight."
                },
                {
                    "id": "mcq_10_p1_5",
                    "question": "The lens formula relating focal length f, image distance v, and object distance u is:",
                    "options": [
                        "A. 1/f = 1/v + 1/u",
                        "B. 1/f = 1/v - 1/u",
                        "C. f = v × u",
                        "D. 1/f = u - v"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 1/f = 1/v - 1/u",
                    "explanation": "Lens formula is 1/f = 1/v - 1/u, while mirror formula is 1/f = 1/v + 1/u."
                }
            ]
        },
        {
            "topic": "Electricity & Ohm's Law (Circuits & Power)",
            "questions": [
                {
                    "id": "mcq_10_p2_1",
                    "question": "Ohm's Law states that at constant temperature, current I is directly proportional to:",
                    "options": [
                        "A. Resistance R",
                        "B. Potential difference V",
                        "C. Electric charge Q",
                        "D. Electric power P"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Potential difference V",
                    "explanation": "Ohm's Law: V ∝ I at constant temperature, leading to V = I·R."
                },
                {
                    "id": "mcq_10_p2_2",
                    "question": "What is the SI unit of electrical resistivity (ρ)?",
                    "options": [
                        "A. Ohm (Ω)",
                        "B. Ohm-meter (Ω·m)",
                        "C. Ohm / meter",
                        "D. Siemens"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Ohm-meter (Ω·m)",
                    "explanation": "ρ = R·A / L => (Ω × m²) / m = Ω·m."
                },
                {
                    "id": "mcq_10_p2_3",
                    "question": "Three identical resistors of 6 Ω each are connected in parallel. What is their equivalent resistance?",
                    "options": [
                        "A. 18 Ω",
                        "B. 6 Ω",
                        "C. 2 Ω",
                        "D. 0.5 Ω"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 2 Ω",
                    "explanation": "1/R_eq = 1/6 + 1/6 + 1/6 = 3/6 = 1/2 => R_eq = 2 Ω."
                },
                {
                    "id": "mcq_10_p2_4",
                    "question": "The commercial unit of electrical energy is 1 kilowatt-hour (kWh). How many Joules is 1 kWh?",
                    "options": [
                        "A. 3.6 × 10⁵ J",
                        "B. 3.6 × 10⁶ J",
                        "C. 1.0 × 10³ J",
                        "D. 7.2 × 10⁶ J"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 3.6 × 10⁶ J",
                    "explanation": "1 kWh = 1000 W × 3600 s = 3,600,000 Joules = 3.6 × 10⁶ J."
                },
                {
                    "id": "mcq_10_p2_5",
                    "question": "Which formula correctly expresses electric power P dissipated in a resistor?",
                    "options": [
                        "A. P = V × I",
                        "B. P = I² × R",
                        "C. P = V² / R",
                        "D. All of the above"
                    ],
                    "correct_index": 3,
                    "correct_option": "D. All of the above",
                    "explanation": "All three expressions (P = VI = I²R = V²/R) are valid mathematical formulations of electric power."
                }
            ]
        },
        {
            "topic": "Magnetic Effects of Electric Current (Electromagnetism)",
            "questions": [
                {
                    "id": "mcq_10_p3_1",
                    "question": "Outside a permanent bar magnet, magnetic field lines emerge from and enter into:",
                    "options": [
                        "A. North pole to South pole",
                        "B. South pole to North pole",
                        "C. East to West",
                        "D. Centre to ends"
                    ],
                    "correct_index": 0,
                    "correct_option": "A. North pole to South pole",
                    "explanation": "Outside the magnet, field lines emerge from the North pole and merge at the South pole, forming closed continuous loops."
                },
                {
                    "id": "mcq_10_p3_2",
                    "question": "Which rule is used to determine the direction of mechanical force on a current-carrying conductor in a magnetic field?",
                    "options": [
                        "A. Fleming's Right-Hand Rule",
                        "B. Fleming's Left-Hand Rule",
                        "C. Right-Hand Thumb Rule",
                        "D. Ampere's Swimming Rule"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Fleming's Left-Hand Rule",
                    "explanation": "Fleming's Left-Hand Rule determines force/motion (Thumb: Force, Forefinger: Magnetic Field, Middle finger: Current)."
                },
                {
                    "id": "mcq_10_p3_3",
                    "question": "A safety fuse wire used in domestic circuits must have:",
                    "options": [
                        "A. High melting point and low resistance",
                        "B. Low melting point and high resistance",
                        "C. High melting point and high resistance",
                        "D. Zero resistance"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Low melting point and high resistance",
                    "explanation": "High resistance generates Joule heat rapidly during an overload, and low melting point melts the wire safely to break the circuit."
                },
                {
                    "id": "mcq_10_p3_4",
                    "question": "What is the standard frequency of Alternating Current (AC) supplied in Indian households?",
                    "options": [
                        "A. 60 Hz",
                        "B. 50 Hz",
                        "C. 100 Hz",
                        "D. 220 Hz"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 50 Hz",
                    "explanation": "In India, domestic AC is supplied at 220 V with an oscillation frequency of 50 Hz (changes direction 100 times per second)."
                },
                {
                    "id": "mcq_10_p3_5",
                    "question": "The strength of the magnetic field inside a long current-carrying solenoid is:",
                    "options": [
                        "A. Zero",
                        "B. Uniform at all points",
                        "C. Decreases towards the centre",
                        "D. Inversely proportional to current"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Uniform at all points",
                    "explanation": "Magnetic field lines inside a solenoid are parallel and equally spaced, indicating a uniform magnetic field."
                }
            ]
        }
    ]

    # Class 10 Chemistry
    ob[(10, "Chemistry")] = [
        {
            "topic": "Chemical Reactions & Equations (Types & Redox)",
            "questions": [
                {
                    "id": "mcq_10_c1_1",
                    "question": "The reaction 2Mg(s) + O₂(g) → 2MgO(s) is an example of which type of reaction?",
                    "options": [
                        "A. Decomposition reaction",
                        "B. Combination reaction",
                        "C. Displacement reaction",
                        "D. Double displacement reaction"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Combination reaction",
                    "explanation": "Two reactants (magnesium and oxygen) combine to form a single product (magnesium oxide)."
                },
                {
                    "id": "mcq_10_c1_2",
                    "question": "When lead nitrate powder is heated in a dry boiling tube, brown fumes of which gas are evolved?",
                    "options": [
                        "A. Oxygen (O₂)",
                        "B. Nitrogen dioxide (NO₂)",
                        "C. Nitrous oxide (N₂O)",
                        "D. Lead oxide vapour"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Nitrogen dioxide (NO₂)",
                    "explanation": "2Pb(NO₃)₂ → 2PbO + 4NO₂↑ (brown fumes) + O₂↑."
                },
                {
                    "id": "mcq_10_c1_3",
                    "question": "Manufacturers flush packets of potato chips with which unreactive gas to prevent rancidity?",
                    "options": [
                        "A. Oxygen",
                        "B. Nitrogen",
                        "C. Carbon dioxide",
                        "D. Chlorine"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Nitrogen",
                    "explanation": "Nitrogen is an inert gas that creates an oxygen-free environment, preventing the oxidation (rancidity) of oils and fats."
                },
                {
                    "id": "mcq_10_c1_4",
                    "question": "In the redox reaction: CuO + H₂ → Cu + H₂O, which substance undergoes reduction?",
                    "options": [
                        "A. H₂",
                        "B. CuO",
                        "C. Cu",
                        "D. H₂O"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. CuO",
                    "explanation": "CuO loses oxygen to form Cu, so CuO undergoes reduction (and acts as the oxidizing agent)."
                },
                {
                    "id": "mcq_10_c1_5",
                    "question": "What colour change is observed when an iron nail is immersed in copper sulphate (CuSO₄) solution for 30 minutes?",
                    "options": [
                        "A. Solution turns blue to yellow",
                        "B. Blue solution turns light pale green with reddish-brown coating on nail",
                        "C. Solution turns colourless with black precipitate",
                        "D. No reaction takes place"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Blue solution turns light pale green with reddish-brown coating on nail",
                    "explanation": "Fe + CuSO₄ → FeSO₄ (green) + Cu (reddish-brown deposit on nail). Displacement occurs because Fe is more reactive than Cu."
                }
            ]
        },
        {
            "topic": "Acids, Bases & Salts (pH & Indicators)",
            "questions": [
                {
                    "id": "mcq_10_c2_1",
                    "question": "What is the pH value of pure neutral water at 25°C?",
                    "options": [
                        "A. 0",
                        "B. 7",
                        "C. 14",
                        "D. 1"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 7",
                    "explanation": "On the pH scale (0 to 14), neutral solutions have a pH of exactly 7 at 25°C."
                },
                {
                    "id": "mcq_10_c2_2",
                    "question": "What natural acid is injected into skin during a honeybee or nettle leaf sting?",
                    "options": [
                        "A. Citric acid",
                        "B. Tartaric acid",
                        "C. Methanoic acid (Formic acid)",
                        "D. Oxalic acid"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Methanoic acid (Formic acid)",
                    "explanation": "Nettle hairs and bee stings inject methanoic acid (HCOOH), causing acute burning sensation treated with mild bases like baking soda."
                },
                {
                    "id": "mcq_10_c2_3",
                    "question": "What is the chemical formula of Plaster of Paris (POP)?",
                    "options": [
                        "A. CaSO₄·2H₂O",
                        "B. CaSO₄·½H₂O",
                        "C. CaSO₄·5H₂O",
                        "D. 2CaSO₄·H₂O"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. CaSO₄·½H₂O",
                    "explanation": "Plaster of Paris is calcium sulphate hemihydrate: CaSO₄·½H₂O (prepared by heating gypsum CaSO₄·2H₂O at 373 K)."
                },
                {
                    "id": "mcq_10_c2_4",
                    "question": "What is the commercial name and chemical formula of Bleaching Powder?",
                    "options": [
                        "A. Calcium hydroxide, Ca(OH)₂",
                        "B. Calcium oxychloride, CaOCl₂",
                        "C. Sodium hypochlorite, NaOCl",
                        "D. Calcium chloride, CaCl₂"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Calcium oxychloride, CaOCl₂",
                    "explanation": "Bleaching powder is CaOCl₂ (calcium oxychloride), synthesized by treating dry slaked lime with chlorine gas."
                },
                {
                    "id": "mcq_10_c2_5",
                    "question": "Natural litmus indicator solution is a purple dye extracted from which organism?",
                    "options": [
                        "A. Fungus",
                        "B. Lichen",
                        "C. Algae",
                        "D. Fern"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Lichen",
                    "explanation": "Litmus is extracted from lichens, a symbiotic association of an alga and a fungus belonging to the Thallophyta division."
                }
            ]
        },
        {
            "topic": "Carbon and its Compounds (Functional Groups & Reactions)",
            "questions": [
                {
                    "id": "mcq_10_c3_1",
                    "question": "What is the general formula for the homologous series of Alkanes?",
                    "options": [
                        "A. CnH2n",
                        "B. CnH2n+2",
                        "C. CnH2n-2",
                        "D. CnHn"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. CnH2n+2",
                    "explanation": "Alkanes are saturated hydrocarbons with single bonds, represented by CnH2n+2 (e.g. CH₄, C₂H₆)."
                },
                {
                    "id": "mcq_10_c3_2",
                    "question": "Which functional group is present in aldehydes like ethanal?",
                    "options": [
                        "A. -OH",
                        "B. -CHO",
                        "C. -COOH",
                        "D. -CO-"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -CHO",
                    "explanation": "The aldehyde functional group is -CHO, alcohol is -OH, carboxylic acid is -COOH, and ketone is -CO-."
                },
                {
                    "id": "mcq_10_c3_3",
                    "question": "When ethanoic acid reacts with absolute ethanol in the presence of concentrated sulphuric acid, what sweet-smelling compound is formed?",
                    "options": [
                        "A. Methane",
                        "B. Ester (Ethyl ethanoate)",
                        "C. Soap",
                        "D. Acetone"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Ester (Ethyl ethanoate)",
                    "explanation": "CH₃COOH + C₂H₅OH (in conc H₂SO₄) → CH₃COOC₂H₅ (sweet ester) + H₂O. This reaction is esterification."
                },
                {
                    "id": "mcq_10_c3_4",
                    "question": "In the cleansing action of soap, radial clusters of soap molecules with hydrocarbon tails pointing inward are called:",
                    "options": [
                        "A. Polymers",
                        "B. Micelles",
                        "C. Emulsions",
                        "D. Colloids"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Micelles",
                    "explanation": "Soap molecules form spherical micelles with hydrophobic tails oriented inwards trapping grease/dirt, and ionic heads facing outwards in water."
                },
                {
                    "id": "mcq_10_c3_5",
                    "question": "Which allotrope of carbon has a rigid three-dimensional tetrahedral cage lattice, making it the hardest natural substance?",
                    "options": [
                        "A. Graphite",
                        "B. Buckminsterfullerene (C-60)",
                        "C. Diamond",
                        "D. Carbon nanotube"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. Diamond",
                    "explanation": "In diamond, each carbon atom is sp³ hybridized and covalently bonded to four other carbon atoms in a tetrahedral structure."
                }
            ]
        }
    ]

    # Class 10 Mathematics
    ob[(10, "Mathematics")] = [
        {
            "topic": "Real Numbers & Fundamental Theorem of Arithmetic",
            "questions": [
                {
                    "id": "mcq_10_m1_1",
                    "question": "For any two positive integers a and b, which relationship between their HCF and LCM holds true?",
                    "options": [
                        "A. HCF(a, b) + LCM(a, b) = a × b",
                        "B. HCF(a, b) × LCM(a, b) = a × b",
                        "C. HCF(a, b) / LCM(a, b) = a + b",
                        "D. LCM(a, b) - HCF(a, b) = a × b"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. HCF(a, b) × LCM(a, b) = a × b",
                    "explanation": "Product of two positive integers equals the product of their HCF and LCM: HCF(a, b) × LCM(a, b) = a × b."
                },
                {
                    "id": "mcq_10_m1_2",
                    "question": "If two integers a and b have HCF(a, b) = 1, then the integers are defined as:",
                    "options": [
                        "A. Twin primes",
                        "B. Co-prime integers",
                        "C. Composite integers",
                        "D. Perfect numbers"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Co-prime integers",
                    "explanation": "Two positive integers are coprime (or relatively prime) if their only common positive factor is 1."
                },
                {
                    "id": "mcq_10_m1_3",
                    "question": "The decimal expansion of 13 / (2² × 5³) terminates after how many decimal places?",
                    "options": [
                        "A. 1 place",
                        "B. 2 places",
                        "C. 3 places",
                        "D. 5 places"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 3 places",
                    "explanation": "The maximum power of 2 or 5 in the denominator is 3 (5³), so it terminates after max(2, 3) = 3 decimal places."
                },
                {
                    "id": "mcq_10_m1_4",
                    "question": "The number (3 + 2√5) is:",
                    "options": [
                        "A. A rational number",
                        "B. An irrational number",
                        "C. An integer",
                        "D. A natural number"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. An irrational number",
                    "explanation": "The sum of a rational number (3) and an irrational number (2√5) is always an irrational number."
                },
                {
                    "id": "mcq_10_m1_5",
                    "question": "The Fundamental Theorem of Arithmetic asserts that every composite number can be uniquely factored as a product of:",
                    "options": [
                        "A. Consecutive integers",
                        "B. Prime powers",
                        "C. Even numbers",
                        "D. Fractions"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Prime powers",
                    "explanation": "Every composite number can be factored uniquely as a product of primes, apart from the order in which the prime factors occur."
                }
            ]
        },
        {
            "topic": "Quadratic Equations & Discriminant Nature of Roots",
            "questions": [
                {
                    "id": "mcq_10_m2_1",
                    "question": "What is the formula for the discriminant D of the quadratic equation ax² + bx + c = 0?",
                    "options": [
                        "A. D = b² + 4ac",
                        "B. D = b² - 4ac",
                        "C. D = 4ac - b²",
                        "D. D = b - 4ac"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. D = b² - 4ac",
                    "explanation": "The discriminant is D = b² - 4ac."
                },
                {
                    "id": "mcq_10_m2_2",
                    "question": "If discriminant D = b² - 4ac > 0 and is not a perfect square, the roots are:",
                    "options": [
                        "A. Real and equal",
                        "B. Real, distinct, and irrational",
                        "C. Imaginary (no real roots)",
                        "D. Zero"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. Real, distinct, and irrational",
                    "explanation": "When D > 0 and not a square, the quadratic formula yields two distinct real roots that are irrational conjugates."
                },
                {
                    "id": "mcq_10_m2_3",
                    "question": "What are the roots of the quadratic equation x² - 5x + 6 = 0?",
                    "options": [
                        "A. 1 and 6",
                        "B. 2 and 3",
                        "C. -2 and -3",
                        "D. -1 and -6"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 2 and 3",
                    "explanation": "Factorizing: (x - 2)(x - 3) = 0 => x = 2 and x = 3."
                },
                {
                    "id": "mcq_10_m2_4",
                    "question": "If the quadratic equation 2x² - kx + 2 = 0 has two equal real roots, find the value(s) of k:",
                    "options": [
                        "A. k = ±2",
                        "B. k = ±4",
                        "C. k = ±8",
                        "D. k = 0"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. k = ±4",
                    "explanation": "For equal roots, D = 0 => (-k)² - 4(2)(2) = 0 => k² - 16 = 0 => k = ±4."
                },
                {
                    "id": "mcq_10_m2_5",
                    "question": "A polynomial equation of degree 2 (quadratic) can have at most how many real roots?",
                    "options": [
                        "A. 1",
                        "B. 2",
                        "C. 3",
                        "D. Infinitely many"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 2",
                    "explanation": "By the Fundamental Theorem of Algebra, an equation of degree n has at most n roots. Hence quadratic has at most 2 roots."
                }
            ]
        },
        {
            "topic": "Arithmetic Progressions (AP Terms & Sums)",
            "questions": [
                {
                    "id": "mcq_10_m3_1",
                    "question": "What is the common difference d of the AP: 10, 7, 4, 1, -2...?",
                    "options": [
                        "A. 3",
                        "B. -3",
                        "C. 4",
                        "D. -4"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. -3",
                    "explanation": "Common difference d = a₂ - a₁ = 7 - 10 = -3."
                },
                {
                    "id": "mcq_10_m3_2",
                    "question": "What is the 10th term (a₁₀) of the AP: 2, 7, 12, 17...?",
                    "options": [
                        "A. 45",
                        "B. 47",
                        "C. 50",
                        "D. 52"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 47",
                    "explanation": "Here a = 2, d = 5. an = a + (n - 1)d => a₁₀ = 2 + (9 × 5) = 2 + 45 = 47."
                },
                {
                    "id": "mcq_10_m3_3",
                    "question": "What is the sum of the first n positive natural numbers (1 + 2 + 3 + ... + n)?",
                    "options": [
                        "A. n²",
                        "B. n(n + 1) / 2",
                        "C. n(n - 1) / 2",
                        "D. 2n(n + 1)"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. n(n + 1) / 2",
                    "explanation": "Using AP sum formula Sn = n/2 [first + last] = n(n + 1) / 2."
                },
                {
                    "id": "mcq_10_m3_4",
                    "question": "If the nth term of an AP is given by a_n = 3n + 1, what is its common difference d?",
                    "options": [
                        "A. 1",
                        "B. 3",
                        "C. 4",
                        "D. 2"
                    ],
                    "correct_index": 1,
                    "correct_option": "B. 3",
                    "explanation": "a₁ = 3(1) + 1 = 4; a₂ = 3(2) + 1 = 7. Difference d = 7 - 4 = 3 (the coefficient of n)."
                },
                {
                    "id": "mcq_10_m3_5",
                    "question": "In an AP, if first term a = 5, common difference d = 3, and the nth term a_n = 50, what is n?",
                    "options": [
                        "A. 14",
                        "B. 15",
                        "C. 16",
                        "D. 17"
                    ],
                    "correct_index": 2,
                    "correct_option": "C. 16",
                    "explanation": "50 = 5 + (n - 1) × 3 => 45 = 3(n - 1) => n - 1 = 15 => n = 16."
                }
            ]
        }
    ]

    return ob


def get_objective_question_set(subject, student_class, custom_topic="", set_index=0):
    """
    Returns 5 objective questions (MCQs) for the specified subject and class,
    supporting set rotation, 4 options each, correct answer verification, and explanations.
    """
    ob = get_full_objective_bank()
    key = (int(student_class), str(subject).strip())

    if custom_topic and len(custom_topic.strip()) > 0:
        topic_clean = custom_topic.strip()
        custom_sets = [
            {
                "topic": f"{topic_clean} (Fundamental Concepts & Definitions)",
                "questions": [
                    {
                        "id": "mcq_cust_1",
                        "question": f"Which fundamental scientific principle or law governs '{topic_clean}'?",
                        "options": [
                            f"A. Conservation of energy and equilibrium principles in {topic_clean}",
                            "B. Dalton's atomic theory exclusively",
                            "C. Newton's universal law of gravitation exclusively",
                            "D. Hooke's law of elasticity"
                        ],
                        "correct_index": 0,
                        "correct_option": f"A. Conservation of energy and equilibrium principles in {topic_clean}",
                        "explanation": f"Understanding {topic_clean} relies on foundational conservation laws and physical equilibrium."
                    },
                    {
                        "id": "mcq_cust_2",
                        "question": f"What is the standard measurement unit or dimension typically utilized when calculating '{topic_clean}'?",
                        "options": [
                            "A. Standard SI base or derived units (e.g. Joules, Newtons, Pascals, or dimensionless ratio)",
                            "B. Light years",
                            "C. Angstroms only",
                            "D. Amperes per square second"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Standard SI base or derived units (e.g. Joules, Newtons, Pascals, or dimensionless ratio)",
                        "explanation": f"Scientific measurements of {topic_clean} strictly adhere to standard SI units."
                    },
                    {
                        "id": "mcq_cust_3",
                        "question": f"Which of the following conditions most significantly affects the behavior of '{topic_clean}'?",
                        "options": [
                            "A. Surrounding temperature, pressure, and medium properties",
                            "B. Colour of the laboratory container",
                            "C. Day of the week",
                            "D. Atmospheric nitrogen percentage only"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Surrounding temperature, pressure, and medium properties",
                        "explanation": f"Thermodynamic parameters and material properties directly govern the experimental behavior of {topic_clean}."
                    },
                    {
                        "id": "mcq_cust_4",
                        "question": f"In daily life or engineering applications, '{topic_clean}' is directly utilized in:",
                        "options": [
                            f"A. Designing optimized instruments, mechanical devices, or chemical processes",
                            "B. Only theoretical philosophical discussions",
                            "C. Measuring planetary orbits only",
                            "D. Ancient calendar creation"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Designing optimized instruments, mechanical devices, or chemical processes",
                        "explanation": f"The principles of {topic_clean} provide direct engineering and practical utility in modern technology."
                    },
                    {
                        "id": "mcq_cust_5",
                        "question": f"When plotting experimental data for '{topic_clean}', a linear relationship between variables indicates:",
                        "options": [
                            "A. Direct proportionality between the observed variables",
                            "B. Inverse exponential decay",
                            "C. Complete absence of physical interaction",
                            "D. Measurement failure"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Direct proportionality between the observed variables",
                        "explanation": "A straight-line graph passing through or offset from the origin indicates direct mathematical proportionality."
                    }
                ]
            },
            {
                "topic": f"{topic_clean} (Advanced Analysis & Applications)",
                "questions": [
                    {
                        "id": "mcq_cust_b1",
                        "question": f"What is the primary assumption made when deriving theoretical equations for '{topic_clean}'?",
                        "options": [
                            "A. Idealized conditions with negligible external dissipative losses",
                            "B. The system operates in absolute vacuum at all times",
                            "C. Temperature is absolute zero",
                            "D. Materials have zero density"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Idealized conditions with negligible external dissipative losses",
                        "explanation": f"Initial theoretical models for {topic_clean} simplify conditions by neglecting friction and resistive losses."
                    },
                    {
                        "id": "mcq_cust_b2",
                        "question": f"If one of the primary input parameters in '{topic_clean}' is doubled, what happens to the output in a linear system?",
                        "options": [
                            "A. Output is doubled",
                            "B. Output is halved",
                            "C. Output quadruples",
                            "D. Output remains unchanged"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Output is doubled",
                        "explanation": "In any first-order linear relationship, doubling the independent variable doubles the response."
                    },
                    {
                        "id": "mcq_cust_b3",
                        "question": f"Which mathematical tool is most helpful when analyzing rates of change in '{topic_clean}'?",
                        "options": [
                            "A. Differential slope analysis (Δy / Δx)",
                            "B. Roman numerals",
                            "C. Venn diagrams",
                            "D. Histograms only"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. Differential slope analysis (Δy / Δx)",
                        "explanation": "Rates of change in scientific phenomena are analyzed using gradients and differentiation."
                    },
                    {
                        "id": "mcq_cust_b4",
                        "question": f"Why is safety and error analysis essential when experimentally verifying '{topic_clean}'?",
                        "options": [
                            "A. To distinguish real physical signals from instrumental uncertainties",
                            "B. To prove theory wrong arbitrarily",
                            "C. Only to satisfy lab reports",
                            "D. To avoid mathematical calculation"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. To distinguish real physical signals from instrumental uncertainties",
                        "explanation": "Rigorous error analysis ensures experimental findings are reliable and statistically valid."
                    },
                    {
                        "id": "mcq_cust_b5",
                        "question": f"Which of the following best summarizes the core importance of '{topic_clean}' for students?",
                        "options": [
                            "A. It bridges theoretical scientific laws with practical everyday applications",
                            "B. It only appears in textbook definitions",
                            "C. It cannot be tested experimentally",
                            "D. It contradicts modern science"
                        ],
                        "correct_index": 0,
                        "correct_option": "A. It bridges theoretical scientific laws with practical everyday applications",
                        "explanation": f"Mastery of {topic_clean} fosters conceptual reasoning and practical problem-solving skills."
                    }
                ]
            }
        ]
        chosen = custom_sets[set_index % len(custom_sets)]
        return {
            "topic_title": chosen["topic"],
            "questions": chosen["questions"],
            "total_sets": len(custom_sets)
        }

    sets = ob.get(key)
    if not sets:
        sets = ob.get((9, subject), ob.get((9, "Physics")))

    total_sets = len(sets)
    selected_set = sets[set_index % total_sets]

    return {
        "topic_title": selected_set["topic"],
        "questions": selected_set["questions"],
        "total_sets": total_sets
    }
