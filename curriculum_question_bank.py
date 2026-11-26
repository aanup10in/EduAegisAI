"""
Curriculum Question Bank and Dynamic Question Set Generator for EduAegis
Covers Classes 8th, 9th, and 10th across Physics, Chemistry, and Mathematics
"""

def get_full_question_bank():
    qb = {}

    # =========================================================================
    # CLASS 8
    # =========================================================================
    qb[(8, "Physics")] = [
        {
            "topic": "Force & Pressure (Contact & Non-contact Forces)",
            "questions": [
                {
                    "id": "q1",
                    "text": "Define Force. Distinguish between contact and non-contact forces giving two examples of each.",
                    "marks": 5,
                    "exemplar": "A force is a push or pull on an object resulting from its interaction with another object. Contact forces occur when two interacting bodies physically touch (e.g. muscular force, frictional force). Non-contact forces act without physical contact across space (e.g. gravitational force, magnetic force, electrostatic force).",
                    "avg_ans": "Force is push or pull. Contact forces touch like friction and muscular force. Non-contact forces act from distance like gravity and magnets.",
                    "keywords": ["force", "push", "pull", "contact", "non-contact", "muscular", "friction", "gravitational", "magnetic"]
                },
                {
                    "id": "q2",
                    "text": "Why do deep-sea divers wear specially designed pressurized diving suits?",
                    "marks": 3,
                    "exemplar": "Liquid pressure increases with depth due to the weight of the water column above. At great depths, intense hydrostatic pressure can crush the human body. Pressurized suits withstand this immense pressure and maintain normal atmospheric breathing conditions.",
                    "avg_ans": "Water pressure increases with depth and can crush human body. Diving suit protects diver from high water pressure.",
                    "keywords": ["pressure", "depth", "water", "increase", "crush", "protect", "suit", "column"]
                },
                {
                    "id": "q3",
                    "text": "Explain why wide wooden or concrete sleepers are placed below railway steel tracks.",
                    "marks": 3,
                    "exemplar": "Pressure is inversely proportional to area (P = F/A). Broad sleepers increase the contact surface area over which the massive weight of the train is distributed. By increasing area, pressure on the underlying ground is greatly reduced, preventing tracks from sinking into the ground.",
                    "avg_ans": "Sleepers increase the surface area so that the pressure of the heavy train is reduced and tracks do not sink in soil.",
                    "keywords": ["area", "pressure", "force", "increase", "reduce", "weight", "sink", "sleepers"]
                },
                {
                    "id": "q4",
                    "text": "A force of 250 N acts perpendicular to a flat surface of area 0.05 m². Calculate the pressure exerted in Pascals.",
                    "marks": 4,
                    "exemplar": "Given: Force F = 250 N, Area A = 0.05 m². Formula: Pressure P = Force / Area = 250 / 0.05 = 5000 N/m² = 5000 Pascals (Pa).",
                    "avg_ans": "P = F / A = 250 / 0.05 = 5000 Pa.",
                    "keywords": ["pressure", "5000", "pascal", "pa", "250", "0.05", "formula", "area"]
                },
                {
                    "id": "q5",
                    "text": "Describe an activity to prove that liquids exert equal pressure at the same depth in all directions.",
                    "marks": 5,
                    "exemplar": "Take a plastic container and drill holes at the exact same horizontal height around its circumference. Fill it with water. Water streams emerge from all holes and strike the floor at identical horizontal distances. This verifies that liquid pressure is equal in all directions at a given depth.",
                    "avg_ans": "Make holes at same height around a bottle and fill water. Water jets travel equal distance from all holes proving equal pressure.",
                    "keywords": ["bottle", "holes", "same height", "same depth", "distance", "equal", "pressure", "stream", "jets"]
                }
            ]
        },
        {
            "topic": "Friction & Streamlining (Rolling vs Sliding)",
            "questions": [
                {
                    "id": "q1",
                    "text": "What is friction? Explain two methods to reduce friction and two methods to increase it.",
                    "marks": 5,
                    "exemplar": "Friction is the opposing force that resists relative motion between surfaces in contact. Methods to reduce: 1) Using lubricants like oil/graphite, 2) Using ball bearings or rollers. Methods to increase: 1) Grooving vehicle tyres and shoe soles with deep treads, 2) Using rough brake pads in bicycles.",
                    "avg_ans": "Friction opposes motion. Reduce by oil and ball bearings. Increase by treaded tyres and spikes on shoes.",
                    "keywords": ["friction", "opposing", "motion", "reduce", "lubricant", "oil", "grease", "increase", "tread", "groove"]
                },
                {
                    "id": "q2",
                    "text": "Why are aeroplanes, birds, and high-speed boats given special streamlined shapes?",
                    "marks": 3,
                    "exemplar": "Fluids (air and water) exert frictional drag on bodies moving through them. Streamlined bodies have pointed fronts and narrow rears, which smooth fluid flow and minimize drag resistance, conserving fuel and allowing higher speeds.",
                    "avg_ans": "Streamlined shapes reduce fluid friction or drag in air and water so they move faster with less energy.",
                    "keywords": ["streamlined", "drag", "fluid", "friction", "air", "reduce", "shape"]
                },
                {
                    "id": "q3",
                    "text": "Why is rolling friction smaller than sliding friction? Where are ball bearings used?",
                    "marks": 4,
                    "exemplar": "In rolling, the area of contact at any instant is microscopic compared to sliding, resulting in minimal interlocking of surface irregularities. Hence rolling friction is much less than sliding. Ball bearings are used in ceiling fans, bicycle axles, and car wheels to convert sliding into rolling.",
                    "avg_ans": "Rolling has less contact area and interlocking than sliding so it is smaller. Ball bearings are used in fans and bicycles.",
                    "keywords": ["rolling", "sliding", "interlocking", "contact", "smaller", "ball bearings", "fan", "bicycle"]
                },
                {
                    "id": "q4",
                    "text": "Explain why truck tyres have deep treads and gymnastics athletes apply chalk powder on hands.",
                    "marks": 4,
                    "exemplar": "Truck tyres have deep treads to increase surface roughness and grip on roads, preventing skidding. Gymnasts apply coarse chalk powder to absorb sweat and increase friction between palms and apparatus for a firm, safe grip.",
                    "avg_ans": "Treads increase road grip to prevent slipping. Gymnasts use chalk to increase hand friction and prevent slipping.",
                    "keywords": ["treads", "grip", "roughness", "friction", "skidding", "chalk", "hands", "gymnast"]
                },
                {
                    "id": "q5",
                    "text": "Why is friction termed a 'necessary evil'? Mention two advantages and two disadvantages.",
                    "marks": 4,
                    "exemplar": "Friction is a necessary evil because life is impossible without it, yet it causes energy waste. Advantages: 1) Allows walking without slipping, 2) Enables writing with pen on paper. Disadvantages: 1) Causes wear and tear of shoe soles and machine gears, 2) Produces unwanted heat wasting fuel.",
                    "avg_ans": "Necessary because we cannot walk or write without it. Evil because it causes wear and tear and wastes energy as heat.",
                    "keywords": ["necessary evil", "walking", "writing", "wear and tear", "heat", "advantage", "disadvantage"]
                }
            ]
        },
        {
            "topic": "Sound, Vibration, Frequency & Audible Range",
            "questions": [
                {
                    "id": "q1",
                    "text": "How is sound produced? Define Frequency, Amplitude, and Time Period with their SI units.",
                    "marks": 5,
                    "exemplar": "Sound is produced by vibrating objects. Frequency is the number of oscillations per second (Hertz, Hz). Amplitude is the maximum displacement from mean position (Metres, m). Time Period is the time taken to complete one oscillation (Seconds, s).",
                    "avg_ans": "Sound is produced by vibration. Frequency is oscillations per second (Hz). Amplitude is max displacement. Time period is time for one oscillation (s).",
                    "keywords": ["vibration", "sound", "frequency", "hertz", "hz", "amplitude", "time period", "seconds", "oscillation"]
                },
                {
                    "id": "q2",
                    "text": "Differentiate between Pitch (shrillness) and Loudness of sound. Which wave parameter determines each?",
                    "marks": 4,
                    "exemplar": "Loudness is determined by the amplitude of vibration; larger amplitude produces louder sound. Pitch (shrillness) is determined by frequency; higher frequency produces a high-pitched shrill voice (e.g. woman's voice), while lower frequency produces deep bass sound.",
                    "avg_ans": "Loudness depends on amplitude. Pitch depends on frequency. High frequency is shrill, large amplitude is loud.",
                    "keywords": ["pitch", "loudness", "amplitude", "frequency", "shrill", "shrillness"]
                },
                {
                    "id": "q3",
                    "text": "Can sound travel through a vacuum? Describe the electric bell-jar experiment.",
                    "marks": 4,
                    "exemplar": "Sound cannot travel through a vacuum as it requires a material medium to propagate. In the bell-jar experiment, an electric bell inside a sealed jar is connected to a vacuum pump. As air is pumped out, the sound becomes fainter and eventually inaudible, proving sound requires a medium.",
                    "avg_ans": "Sound cannot travel in vacuum. When air is sucked from bell jar with vacuum pump, ringing sound stops.",
                    "keywords": ["vacuum", "medium", "bell jar", "pump", "air", "travel", "sound"]
                },
                {
                    "id": "q4",
                    "text": "What is Noise Pollution? State two health hazards and two measures to control it in cities.",
                    "marks": 3,
                    "exemplar": "Noise pollution is presence of unwanted excessive sound in environment. Hazards: Hypertension, insomnia, hearing impairment. Control measures: Silencers in vehicle exhausts, tree planting along roads, prohibition of loud horns near hospitals/schools.",
                    "avg_ans": "Noise pollution is loud unwanted noise. Causes hearing loss and sleep problems. Controlled by silencers and planting trees.",
                    "keywords": ["noise pollution", "unwanted", "hearing", "insomnia", "silencers", "trees", "horns"]
                },
                {
                    "id": "q5",
                    "text": "State the audible range of frequencies for the human ear. Define Infrasonic and Ultrasonic sound.",
                    "marks": 4,
                    "exemplar": "Audible range for human ear is 20 Hz to 20,000 Hz. Infrasonic sound consists of frequencies below 20 Hz (e.g. earthquake waves, rhinoceros communication). Ultrasonic sound consists of frequencies above 20,000 Hz (e.g. bats, ultrasound medical imaging).",
                    "avg_ans": "Audible range is 20 Hz to 20,000 Hz. Infrasonic is below 20 Hz. Ultrasonic is above 20,000 Hz.",
                    "keywords": ["20 hz", "20000 hz", "20,000", "audible", "infrasonic", "ultrasonic", "bats", "earthquake"]
                }
            ]
        }
    ]

    qb[(8, "Chemistry")] = [
        {
            "topic": "Synthetic Fibres, Polymers & Plastics",
            "questions": [
                {
                    "id": "q1",
                    "text": "What are synthetic fibres? Distinguish between thermosetting plastics and thermoplastics with two examples each.",
                    "marks": 5,
                    "exemplar": "Synthetic fibres are man-made fibres prepared from petrochemicals through polymerization. Thermoplastics soften easily upon heating and can be bent and remoulded repeatedly (e.g. Polythene, PVC). Thermosetting plastics, once moulded, cannot be softened by heating (e.g. Bakelite, Melamine).",
                    "avg_ans": "Synthetic fibres are man-made. Thermoplastics soften on heating like PVC. Thermosetting plastics cannot be softened on heating like Bakelite.",
                    "keywords": ["synthetic", "man-made", "polymer", "thermoplastics", "thermosetting", "heating", "bakelite", "pvc", "melamine", "soften"]
                },
                {
                    "id": "q2",
                    "text": "Why is nylon widely used for making climbing ropes, parachutes, and fishing nets?",
                    "marks": 4,
                    "exemplar": "Nylon is fully synthetic, prepared from coal, water, and air. A nylon thread is actually stronger than a steel wire of comparable thickness. It is elastic, lightweight, lustrous, easy to wash, and highly resistant to abrasion and water absorption.",
                    "avg_ans": "Nylon is stronger than steel wire, elastic, lightweight, and does not rot in water, so it is used in ropes.",
                    "keywords": ["nylon", "strong", "steel wire", "elastic", "lightweight", "ropes", "parachutes"]
                },
                {
                    "id": "q3",
                    "text": "Explain the 4R principle for plastic waste management and environmental conservation.",
                    "marks": 4,
                    "exemplar": "The 4R principle stands for: 1) Reduce: Minimize plastic consumption, 2) Reuse: Use plastic containers multiple times, 3) Recycle: Collect and reprocess thermoplastics, 4) Recover: Convert plastic waste into energy or fuel.",
                    "avg_ans": "4R means Reduce, Reuse, Recycle, and Recover to protect environment from plastic pollution.",
                    "keywords": ["reduce", "reuse", "recycle", "recover", "plastic", "waste", "4r"]
                },
                {
                    "id": "q4",
                    "text": "Why is it dangerous to wear synthetic clothes like polyester while working in a kitchen or laboratory?",
                    "marks": 3,
                    "exemplar": "Synthetic fibres melt on heating. If clothes catch fire, the synthetic fabric melts and shrinks, sticking tenaciously to the victim's skin and causing severe, deep burns. Hence, cotton clothes are recommended in kitchens.",
                    "avg_ans": "Synthetic clothes melt on catching fire and stick to the skin causing severe burns.",
                    "keywords": ["melt", "stick", "skin", "burns", "fire", "synthetic", "cotton"]
                },
                {
                    "id": "q5",
                    "text": "What is Melamine? Why is it used for making firemen uniforms and kitchen floor tiles?",
                    "marks": 4,
                    "exemplar": "Melamine is a versatile thermosetting plastic. It resists fire and can tolerate heat better than other plastics. Therefore, it is coated on firemen's uniforms for flame resistance and used in kitchenware and floor tiles.",
                    "avg_ans": "Melamine is a thermosetting plastic that resists fire and tolerates high heat, so used for firemen uniforms and kitchenware.",
                    "keywords": ["melamine", "thermosetting", "fire", "heat", "tolerate", "uniforms", "tiles"]
                }
            ]
        },
        {
            "topic": "Coal, Petroleum & Fractional Distillation",
            "questions": [
                {
                    "id": "q1",
                    "text": "Describe the process of coal formation (Carbonisation) from prehistoric vegetation.",
                    "marks": 5,
                    "exemplar": "About 300 million years ago, dense swamp forests got buried under soil due to natural disasters. Under high temperature and high pressure beneath layers of earth, the dead plant matter was slowly converted into coal. This slow process of conversion of dead vegetation into coal is called Carbonisation.",
                    "avg_ans": "Dead plants buried under soil millions of years ago turned into coal under high pressure and temperature. This is carbonisation.",
                    "keywords": ["carbonisation", "vegetation", "plants", "buried", "high temperature", "high pressure", "coal", "millions of years"]
                },
                {
                    "id": "q2",
                    "text": "Name three products obtained from destructive distillation of coal and state one application of each.",
                    "marks": 4,
                    "exemplar": "1) Coke: Almost pure carbon, used in steel manufacturing and metal extraction. 2) Coal Tar: Thick black liquid used in making synthetic dyes, drugs, and naphthalene balls. 3) Coal Gas: Used as an industrial heating fuel.",
                    "avg_ans": "Coke for steel making. Coal tar for dyes and medicines. Coal gas as fuel.",
                    "keywords": ["coke", "coal tar", "coal gas", "steel", "dyes", "fuel", "destructive distillation"]
                },
                {
                    "id": "q3",
                    "text": "What is Fractional Distillation of petroleum? Name four petroleum fractions and their uses.",
                    "marks": 4,
                    "exemplar": "Fractional distillation separates crude petroleum into fractions based on boiling point differences. Fractions: 1) LPG: Domestic and industrial fuel, 2) Petrol: Motor fuel, 3) Kerosene: Fuel for stoves and jet engines, 4) Bitumen: Road surfacing and paints.",
                    "avg_ans": "Separating petroleum based on boiling points. LPG for cooking, Petrol for cars, Kerosene for jet fuel, Bitumen for roads.",
                    "keywords": ["fractional distillation", "boiling points", "petroleum", "lpg", "petrol", "kerosene", "bitumen", "fuel"]
                },
                {
                    "id": "q4",
                    "text": "Why is petroleum referred to as 'Black Gold'? Why are fossil fuels non-renewable?",
                    "marks": 3,
                    "exemplar": "Petroleum is called 'Black Gold' due to its dark crude color and immense commercial and industrial value. Fossil fuels are non-renewable because nature took millions of years to form them, while current human consumption will exhaust known reserves within a few decades.",
                    "avg_ans": "Black Gold because it is black and very valuable like gold. Non-renewable because it takes millions of years to form and cannot be remade quickly.",
                    "keywords": ["black gold", "commercial", "valuable", "non-renewable", "exhaust", "millions of years"]
                },
                {
                    "id": "q5",
                    "text": "What is CNG (Compressed Natural Gas)? Why is it favored over petrol and diesel in public transport?",
                    "marks": 4,
                    "exemplar": "CNG is natural gas (mainly methane) stored under high pressure. It is favored because: 1) It burns completely leaving no smoke or unburnt residue, 2) Produces negligible carbon monoxide and sulphur dioxide, 3) Is cheaper and causes less engine corrosion.",
                    "avg_ans": "CNG is compressed natural gas. It is a clean fuel that produces no smoke and less pollution than petrol or diesel.",
                    "keywords": ["cng", "compressed natural gas", "methane", "clean fuel", "smoke", "pollution", "residue"]
                }
            ]
        },
        {
            "topic": "Combustion, Types of Flame & Calorific Value",
            "questions": [
                {
                    "id": "q1",
                    "text": "Define Combustion. State three essential conditions necessary for combustion to occur.",
                    "marks": 5,
                    "exemplar": "Combustion is a chemical process in which a substance reacts with oxygen to produce heat and light. Essential conditions: 1) Presence of a combustible substance (fuel), 2) Continuous supply of oxygen (supporter of combustion), 3) Heating substance to its ignition temperature.",
                    "avg_ans": "Combustion is burning in oxygen to give heat. Conditions: combustible fuel, oxygen supply, and reaching ignition temperature.",
                    "keywords": ["combustion", "chemical process", "oxygen", "heat", "fuel", "ignition temperature", "supporter"]
                },
                {
                    "id": "q2",
                    "text": "Describe the three distinct zones of a candle flame with temperature and color characteristics.",
                    "marks": 4,
                    "exemplar": "1) Outermost Zone: Blue color, complete combustion, hottest zone. 2) Middle Zone: Yellow/luminous, incomplete combustion due to limited air, moderately hot. 3) Innermost Zone: Dark black, unburnt wax vapors, least hot zone.",
                    "avg_ans": "Outer zone is blue and hottest with complete combustion. Middle zone is yellow and moderately hot. Inner zone is black with unburnt wax and least hot.",
                    "keywords": ["outermost", "blue", "hottest", "complete combustion", "middle", "yellow", "innermost", "black", "unburnt"]
                },
                {
                    "id": "q3",
                    "text": "What is Calorific Value? A fuel sample produces 180,000 kJ heat on burning 4.5 kg. Calculate its calorific value.",
                    "marks": 4,
                    "exemplar": "Calorific value is the amount of heat energy released on complete combustion of 1 kg of fuel (kJ/kg). Given: Total heat = 180,000 kJ, Mass = 4.5 kg. Calorific Value = 180,000 / 4.5 = 40,000 kJ/kg.",
                    "avg_ans": "Calorific value = Heat / Mass = 180000 / 4.5 = 40,000 kJ/kg.",
                    "keywords": ["calorific value", "40000", "40,000", "kj/kg", "180000", "4.5", "heat energy"]
                },
                {
                    "id": "q4",
                    "text": "Why should water never be used to extinguish fires caused by electrical short-circuits or petrol/oil?",
                    "marks": 3,
                    "exemplar": "Ordinary water conducts electricity, which can electrocute firefighters. For oil and petrol fires, water is denser than oil; oil floats on water and continues burning, spreading the fire further. CO₂ extinguishers must be used instead.",
                    "avg_ans": "Water conducts electricity and can shock people. Oil floats on water so water spreads oil fire instead of extinguishing.",
                    "keywords": ["water", "conducts electricity", "electrocution", "oil floats", "spreads", "co2", "fire"]
                },
                {
                    "id": "q5",
                    "text": "Differentiate between Rapid Combustion, Spontaneous Combustion, and Explosion with one example each.",
                    "marks": 4,
                    "exemplar": "1) Rapid: Substance burns rapidly producing heat and light upon external ignition (e.g. gas stove, matchstick). 2) Spontaneous: Substance suddenly bursts into flame without external heat (e.g. white phosphorus, coal dust in mines). 3) Explosion: Sudden reaction producing immense heat, light, sound, and gas volume (e.g. firecrackers).",
                    "avg_ans": "Rapid needs matchstick like cooking gas. Spontaneous burns on its own like phosphorus. Explosion gives heat, light and loud sound like firecrackers.",
                    "keywords": ["rapid", "spontaneous", "explosion", "phosphorus", "gas", "firecrackers", "external heat"]
                }
            ]
        }
    ]

    qb[(8, "Mathematics")] = [
        {
            "topic": "Rational Numbers & Linear Equations in One Variable",
            "questions": [
                {
                    "id": "q1",
                    "text": "State the Distributive Property of multiplication over addition for rational numbers. Verify for a = -1/2, b = 2/3, c = 1/4.",
                    "marks": 5,
                    "exemplar": "Distributive Property: a × (b + c) = (a × b) + (a × c). LHS: -1/2 × (2/3 + 1/4) = -1/2 × (11/12) = -11/24. RHS: (-1/2 × 2/3) + (-1/2 × 1/4) = -1/3 + (-1/8) = -8/24 - 3/24 = -11/24. LHS = RHS, verified.",
                    "avg_ans": "a(b+c) = ab + ac. LHS = -1/2 * (2/3 + 1/4) = -11/24. RHS = -1/3 - 1/8 = -11/24. LHS = RHS verified.",
                    "keywords": ["distributive", "-11/24", "lhs", "rhs", "verified", "property", "rational"]
                },
                {
                    "id": "q2",
                    "text": "Solve the linear equation: 5x + 9 = 5 + 3x and verify the solution.",
                    "marks": 3,
                    "exemplar": "Transposing variables: 5x - 3x = 5 - 9 => 2x = -4 => x = -4/2 = -2. Verification: LHS = 5(-2) + 9 = -10 + 9 = -1. RHS = 5 + 3(-2) = 5 - 6 = -1. LHS = RHS.",
                    "avg_ans": "5x - 3x = 5 - 9 => 2x = -4 => x = -2. Check: 5(-2)+9 = -1, 5+3(-2) = -1.",
                    "keywords": ["x = -2", "-2", "2x = -4", "lhs", "rhs", "verified", "transposing"]
                },
                {
                    "id": "q3",
                    "text": "The perimeter of a rectangular swimming pool is 154 m. Its length is 2 m more than twice its breadth. Find length and breadth.",
                    "marks": 4,
                    "exemplar": "Let breadth = x m. Length = 2x + 2 m. Perimeter = 2(l + b) = 2(2x + 2 + x) = 2(3x + 2) = 6x + 4 = 154. 6x = 150 => x = 25 m. Breadth = 25 m, Length = 2(25) + 2 = 52 m.",
                    "avg_ans": "Breadth = x, Length = 2x+2. 2(3x+2) = 154 => 6x = 150 => x = 25. Breadth = 25 m, Length = 52 m.",
                    "keywords": ["breadth = 25", "length = 52", "25", "52", "perimeter", "154", "2x + 2"]
                },
                {
                    "id": "q4",
                    "text": "Represent -2/11, -5/11, and -9/11 on a single number line. Explain the scale chosen.",
                    "marks": 4,
                    "exemplar": "Divide the unit interval between 0 and -1 into 11 equal subdivisions. Each mark represents -1/11. Count 2 marks left of 0 for -2/11, 5 marks left for -5/11, and 9 marks left for -9/11.",
                    "avg_ans": "Divide 0 to -1 into 11 parts. Mark -2/11 at 2nd point, -5/11 at 5th point, -9/11 at 9th point to the left of 0.",
                    "keywords": ["number line", "11 equal", "parts", "left of 0", "-2/11", "-5/11", "-9/11", "unit"]
                },
                {
                    "id": "q5",
                    "text": "The sum of three consecutive multiples of 8 is 888. Find these three multiples.",
                    "marks": 4,
                    "exemplar": "Let consecutive multiples be x, x + 8, and x + 16. Sum: x + (x + 8) + (x + 16) = 888 => 3x + 24 = 888 => 3x = 864 => x = 288. Multiples are 288, 296, and 304.",
                    "avg_ans": "x + (x+8) + (x+16) = 888 => 3x = 864 => x = 288. Numbers are 288, 296, 304.",
                    "keywords": ["288", "296", "304", "888", "3x + 24", "multiples"]
                }
            ]
        },
        {
            "topic": "Quadrilaterals, Polygons & Parallelograms",
            "questions": [
                {
                    "id": "q1",
                    "text": "State the Angle Sum Property of an n-sided polygon. Find the measure of each interior angle of a regular octagon.",
                    "marks": 5,
                    "exemplar": "Sum of interior angles of n-sided polygon = (n - 2) × 180°. For octagon, n = 8. Sum = (8 - 2) × 180° = 6 × 180° = 1080°. Since regular, each interior angle = 1080° / 8 = 135°.",
                    "avg_ans": "Sum = (n-2)*180 = 6*180 = 1080. Each interior angle = 1080 / 8 = 135 degrees.",
                    "keywords": ["(n - 2) * 180", "1080", "135", "octagon", "angle sum", "interior angle"]
                },
                {
                    "id": "q2",
                    "text": "Two adjacent angles of a parallelogram are in the ratio 3:2. Find the measure of all four angles.",
                    "marks": 4,
                    "exemplar": "In a parallelogram, adjacent angles are supplementary (sum = 180°). Let angles be 3x and 2x. 3x + 2x = 180° => 5x = 180° => x = 36°. Angles: 3(36) = 108° and 2(36) = 72°. Opposite angles are equal, so the four angles are 108°, 72°, 108°, 72°.",
                    "avg_ans": "3x + 2x = 180 => 5x = 180 => x = 36. Angles are 108, 72, 108, 72 degrees.",
                    "keywords": ["108", "72", "3x + 2x = 180", "supplementary", "adjacent angles", "parallelogram"]
                },
                {
                    "id": "q3",
                    "text": "Prove that the diagonals of a rectangle are equal in length and bisect each other.",
                    "marks": 4,
                    "exemplar": "In rectangle ABCD, consider triangles ABC and ABD. AB is common side. AD = BC (opposite sides). Angle DAB = Angle CBA = 90°. By SAS congruence, ΔABD ≅ ΔBAC. Therefore, AC = BD (CPCTC). Since rectangle is a parallelogram, diagonals also bisect each other.",
                    "avg_ans": "In ΔABC and ΔABD, AB is common, BC=AD, angle A = angle B = 90. So ΔABC ≅ ΔABD by SAS. AC=BD by CPCT.",
                    "keywords": ["sas", "congruence", "rectangle", "diagonals equal", "cpct", "bisect", "90"]
                },
                {
                    "id": "q4",
                    "text": "In a rhombus ABCD, the diagonals measure 16 cm and 12 cm. Calculate the length of each side of the rhombus.",
                    "marks": 4,
                    "exemplar": "Diagonals of a rhombus bisect each other at right angles (90°). Half-diagonals: AO = 16/2 = 8 cm, BO = 12/2 = 6 cm. In right ΔAOB, using Pythagoras theorem: Side AB = √(8² + 6²) = √(64 + 36) = √100 = 10 cm.",
                    "avg_ans": "Half diagonals are 8 and 6. By Pythagoras: side = √(8² + 6²) = √100 = 10 cm.",
                    "keywords": ["10 cm", "10", "pythagoras", "8", "6", "rhombus", "diagonals bisect at 90", "100"]
                },
                {
                    "id": "q5",
                    "text": "Can a quadrilateral ABCD have angle A = 70°, B = 105°, C = 85°, and D = 110°? Justify using angle sum property.",
                    "marks": 3,
                    "exemplar": "The sum of all four interior angles of any convex quadrilateral must be exactly 360°. Sum = 70° + 105° + 85° + 110° = 370°. Since 370° ≠ 360°, such a quadrilateral cannot exist.",
                    "avg_ans": "Sum = 70 + 105 + 85 + 110 = 370. Sum of quadrilateral must be 360. So this quadrilateral cannot exist.",
                    "keywords": ["370", "360", "cannot exist", "not possible", "sum of angles"]
                }
            ]
        },
        {
            "topic": "Squares, Square Roots & Algebraic Identities",
            "questions": [
                {
                    "id": "q1",
                    "text": "Find the square root of 7056 using long division method. Show all calculation steps.",
                    "marks": 5,
                    "exemplar": "Pair digits from right: 70 56. Largest square ≤ 70 is 8² = 64. Remainder = 6. Bring down 56 -> 656. Double quotient 8 -> 16. 164 × 4 = 656. Remainder = 0. Therefore, √7056 = 84.",
                    "avg_ans": "Using long division on 70 56: 8*8 = 64, remainder 6. Bring down 56 -> 656. 164 * 4 = 656. Square root is 84.",
                    "keywords": ["84", "long division", "7056", "656", "164", "square root"]
                },
                {
                    "id": "q2",
                    "text": "Find the smallest natural number by which 180 must be multiplied so that the product becomes a perfect square.",
                    "marks": 4,
                    "exemplar": "Prime factorisation of 180: 180 = 2 × 2 × 3 × 3 × 5 = 2² × 3² × 5. Prime factor 5 has no pair. To make it a perfect square, 180 must be multiplied by 5. Perfect square = 180 × 5 = 900 (√900 = 30).",
                    "avg_ans": "180 = 2 * 2 * 3 * 3 * 5. Factor 5 is unpaired. Must multiply by 5 to make 900 which is 30².",
                    "keywords": ["5", "unpaired", "prime factorisation", "180", "900", "perfect square"]
                },
                {
                    "id": "q3",
                    "text": "Evaluate using suitable algebraic identities: (a) 103 × 104, (b) (95)². Show formulas applied.",
                    "marks": 4,
                    "exemplar": "(a) (100 + 3)(100 + 4) = 100² + (3+4)100 + (3×4) = 10000 + 700 + 12 = 10712 using (x+a)(x+b) = x² + (a+b)x + ab. (b) (100 - 5)² = 100² - 2(100)(5) + 5² = 10000 - 1000 + 25 = 9025 using (a-b)² = a² - 2ab + b².",
                    "avg_ans": "(a) (100+3)(100+4) = 10000 + 700 + 12 = 10712. (b) (100-5)² = 10000 - 1000 + 25 = 9025.",
                    "keywords": ["10712", "9025", "(x+a)(x+b)", "(a-b)²", "identity", "100"]
                },
                {
                    "id": "q4",
                    "text": "Factorise completely using identities: (a) 49x² - 36y², (b) a² + 10a + 25.",
                    "marks": 4,
                    "exemplar": "(a) (7x)² - (6y)² = (7x - 6y)(7x + 6y) using a² - b² = (a-b)(a+b). (b) a² + 2(a)(5) + 5² = (a + 5)² using a² + 2ab + b² = (a+b)².",
                    "avg_ans": "(a) (7x - 6y)(7x + 6y). (b) (a + 5)².",
                    "keywords": ["(7x - 6y)", "(7x + 6y)", "(a + 5)", "factorise", "identity", "a² - b²"]
                },
                {
                    "id": "q5",
                    "text": "The area of a square field is 60025 m². A cyclist rides around its boundary at 18 km/h. How many seconds will he take to complete one round?",
                    "marks": 3,
                    "exemplar": "Side of square = √60025 = 245 m. Perimeter = 4 × 245 = 980 m. Speed = 18 km/h = 18 × (5/18) = 5 m/s. Time taken = Distance / Speed = 980 / 5 = 196 seconds.",
                    "avg_ans": "Side = √60025 = 245 m. Perimeter = 4*245 = 980 m. Speed = 18 km/h = 5 m/s. Time = 980 / 5 = 196 seconds.",
                    "keywords": ["245", "980", "5 m/s", "196", "seconds", "square field"]
                }
            ]
        }
    ]

    # =========================================================================
    # CLASS 9
    # =========================================================================
    qb[(9, "Physics")] = [
        {
            "topic": "Newton's Laws of Motion & Momentum",
            "questions": [
                {
                    "id": "q1",
                    "text": "State Newton's Second Law of Motion. Derive the formula F = ma defining all SI units.",
                    "marks": 5,
                    "exemplar": "Newton's Second Law states that rate of change of momentum is proportional to applied force in direction of force. p1=mu, p2=mv, Δp=m(v-u). Rate=m(v-u)/t=ma. F=ma. Units: Force in N, mass in kg, acc in m/s².",
                    "avg_ans": "Rate of change of momentum is proportional to force. F = m(v-u)/t = ma. Force in Newtons, mass in kg, acceleration in m/s².",
                    "keywords": ["momentum", "force", "acceleration", "f = ma", "f=ma", "mass", "rate of change", "p1", "p2", "newton", "kg", "m/s"]
                },
                {
                    "id": "q2",
                    "text": "Why does a fielder pull his hands backward while catching a fast cricket ball?",
                    "marks": 3,
                    "exemplar": "Fielder pulls hands back to increase stopping time t. Since F = m(v-u)/t, increasing time decreases the rate of change of momentum, reducing impact force on palms.",
                    "avg_ans": "Pulling hands back increases time taken to stop ball. Higher time decreases the force on hands so hands do not get hurt.",
                    "keywords": ["time", "hand", "hands", "momentum", "force", "impact", "backward", "pull", "hurt", "reduce", "increase time"]
                },
                {
                    "id": "q3",
                    "text": "Define Inertia. Name its three types with daily-life examples and state its measure.",
                    "marks": 3,
                    "exemplar": "Inertia is property resisting change of rest or motion. Types: rest (passengers fall back when bus starts), motion (fall forward when brakes applied), direction (lean sideways when turning). Mass measures inertia.",
                    "avg_ans": "Inertia is tendency to resist change in state. Types are rest, motion, direction. Mass is the measure of inertia.",
                    "keywords": ["inertia", "rest", "motion", "direction", "mass", "resist", "tendency", "property", "oppose"]
                },
                {
                    "id": "q4",
                    "text": "A 1200 kg car slows from 90 km/h to 18 km/h in 4 s. Calculate acceleration and force.",
                    "marks": 5,
                    "exemplar": "u = 90 km/h = 25 m/s, v = 18 km/h = 5 m/s. a = (5-25)/4 = -5 m/s² (retardation). Change in momentum = -24000 kg·m/s. Force = 1200*(-5) = -6000 N.",
                    "avg_ans": "u = 25 m/s, v = 5 m/s. a = (5-25)/4 = -5 m/s². Force = 1200 * -5 = -6000 N.",
                    "keywords": ["acceleration", "force", "velocity", "-5", "5", "6000", "-6000", "retardation", "m/s", "km/h", "25", "1200"]
                },
                {
                    "id": "q5",
                    "text": "State Newton's Third Law. Why do action and reaction forces not cancel each other?",
                    "marks": 4,
                    "exemplar": "To every action there is equal and opposite reaction. They do not cancel because action and reaction act on TWO DIFFERENT BODIES simultaneously, never on the same body.",
                    "avg_ans": "Action and reaction are equal and opposite. They do not cancel because they act on two different bodies.",
                    "keywords": ["action", "reaction", "different", "two bodies", "equal", "opposite", "cancel", "pair"]
                }
            ]
        },
        {
            "topic": "Gravitation, Floatation & Archimedes' Principle",
            "questions": [
                {
                    "id": "q1",
                    "text": "State the Universal Law of Gravitation. Derive its formula and state the value and SI unit of G.",
                    "marks": 5,
                    "exemplar": "Every object attracts every other object with a force directly proportional to the product of their masses and inversely proportional to the square of the distance between them: F = G(m1*m2)/r². G = 6.673 × 10^-11 N·m²/kg².",
                    "avg_ans": "F = G m1 m2 / r². G is gravitational constant = 6.67 * 10^-11 N m²/kg².",
                    "keywords": ["universal law", "gravitation", "f = g", "m1*m2", "r²", "distance", "6.67", "10^-11", "n m²/kg²"]
                },
                {
                    "id": "q2",
                    "text": "Differentiate between Mass (m) and Weight (W) on four distinct scientific parameters.",
                    "marks": 4,
                    "exemplar": "1) Mass is quantity of matter; Weight is gravitational force (W = mg). 2) Mass is scalar; Weight is vector. 3) Mass is constant everywhere; Weight varies with g. 4) Mass unit is kg; Weight unit is Newton (N).",
                    "avg_ans": "Mass is matter in body, scalar, unit kg, constant everywhere. Weight is force of gravity, vector, unit Newton, changes with place.",
                    "keywords": ["mass", "weight", "scalar", "vector", "kg", "newton", "constant", "varies", "mg"]
                },
                {
                    "id": "q3",
                    "text": "State Archimedes' Principle. Explain why an iron nail sinks in water but a huge iron ship floats.",
                    "marks": 4,
                    "exemplar": "Archimedes' principle: When a body is immersed in fluid, it experiences an upward buoyant force equal to the weight of fluid displaced. A small nail displaces less water than its weight, so it sinks. A hollow ship displaces a huge volume of water whose weight exceeds the ship's weight, so it floats.",
                    "avg_ans": "Upward buoyant force equals weight of liquid displaced. Nail displaces little water so sinks. Ship is hollow and displaces huge water so buoyant force makes it float.",
                    "keywords": ["archimedes", "buoyant force", "upthrust", "displaced", "volume", "nail sinks", "ship floats", "density"]
                },
                {
                    "id": "q4",
                    "text": "An object weighs 10 N on Earth. What is its weight on the Moon? Explain the reason.",
                    "marks": 3,
                    "exemplar": "Acceleration due to gravity on the Moon is 1/6th that on Earth (g_moon = g_earth / 6). Therefore, Weight on Moon = 10 N / 6 = 1.67 N. The Moon has less mass, producing weaker gravitational pull.",
                    "avg_ans": "Weight on Moon = 10 / 6 = 1.67 N because moon's gravity is one-sixth of earth's gravity.",
                    "keywords": ["1/6", "one-sixth", "1.67", "1.66", "gravity", "moon", "weaker"]
                },
                {
                    "id": "q5",
                    "text": "What is Relative Density? The relative density of silver is 10.8. Find silver's density in SI units (water density = 1000 kg/m³).",
                    "marks": 4,
                    "exemplar": "Relative Density = Density of substance / Density of water at 4°C. It is dimensionless. Density of silver = Relative Density × Density of water = 10.8 × 1000 kg/m³ = 10,800 kg/m³.",
                    "avg_ans": "Relative density = density of substance / density of water. Silver density = 10.8 * 1000 = 10800 kg/m³.",
                    "keywords": ["relative density", "10800", "10,800", "kg/m³", "water", "dimensionless"]
                }
            ]
        },
        {
            "topic": "Work, Energy, Conservation of Energy & Power",
            "questions": [
                {
                    "id": "q1",
                    "text": "Define Kinetic Energy. Derive the formula KE = 1/2 mv² for a body of mass m moving with velocity v.",
                    "marks": 5,
                    "exemplar": "Kinetic energy is the energy possessed by a body due to its motion. Work done = F × s. Using v² - u² = 2as => s = (v² - u²)/(2a). F = ma. Work = ma × (v² - u²)/(2a) = 1/2 m(v² - u²). Starting from rest (u=0), KE = 1/2 mv².",
                    "avg_ans": "Kinetic energy is energy of motion. Work = F*s = ma*(v²/2a) = 1/2 mv² when starting from rest.",
                    "keywords": ["kinetic energy", "1/2 mv²", "motion", "work", "v² - u² = 2as", "f = ma", "derivation"]
                },
                {
                    "id": "q2",
                    "text": "State the Law of Conservation of Energy. Show that total mechanical energy of a free-falling body is constant.",
                    "marks": 5,
                    "exemplar": "Energy cannot be created or destroyed, only transformed from one form to another. At height h: PE = mgh, KE = 0, Total = mgh. At midway (h-x): PE = mg(h-x), v² = 2gx => KE = mgx, Total = mgh. Just before ground: PE = 0, v² = 2gh => KE = mgh, Total = mgh. Constant at all points.",
                    "avg_ans": "Energy cannot be created or destroyed. At top total = mgh. At midway total = mgh. At bottom total = mgh. Always constant.",
                    "keywords": ["conservation of energy", "mgh", "potential energy", "kinetic energy", "free fall", "constant", "total mechanical energy"]
                },
                {
                    "id": "q3",
                    "text": "An electric heater of 1500 W operates for 10 hours daily. Calculate the electrical units (kWh) consumed in 30 days.",
                    "marks": 4,
                    "exemplar": "Power P = 1500 W = 1.5 kW. Time daily = 10 hours. Daily energy = 1.5 kW × 10 h = 15 kWh. In 30 days = 15 × 30 = 450 kWh (450 commercial units).",
                    "avg_ans": "Power = 1.5 kW. Daily = 1.5 * 10 = 15 kWh. Month = 15 * 30 = 450 units.",
                    "keywords": ["450", "kwh", "units", "1.5 kw", "1500 w", "energy consumed", "power"]
                },
                {
                    "id": "q4",
                    "text": "Differentiate between Transverse and Longitudinal waves with one example of each.",
                    "marks": 3,
                    "exemplar": "Transverse waves: Particles vibrate perpendicular to wave propagation; forms crests and troughs (e.g. light wave, ripples on water). Longitudinal waves: Particles vibrate parallel to wave propagation; forms compressions and rarefactions (e.g. sound waves in air).",
                    "avg_ans": "Transverse vibrate perpendicular with crests and troughs like light. Longitudinal vibrate parallel with compressions and rarefactions like sound.",
                    "keywords": ["transverse", "longitudinal", "perpendicular", "parallel", "crests", "troughs", "compressions", "rarefactions", "sound"]
                },
                {
                    "id": "q5",
                    "text": "What is an Echo? Calculate the minimum distance required between a person and a wall to hear an echo (speed of sound = 344 m/s).",
                    "marks": 3,
                    "exemplar": "An echo is repetition of sound caused by reflection from an obstacle. Sensation of sound persists in ear for 0.1 s. Total round trip distance = v × t = 344 × 0.1 = 34.4 m. Minimum distance to obstacle = 34.4 / 2 = 17.2 metres.",
                    "avg_ans": "Echo is reflected sound. Persistence of hearing is 0.1 s. Distance = (344 * 0.1) / 2 = 17.2 metres.",
                    "keywords": ["echo", "17.2", "17.2 m", "0.1 s", "persistence", "344", "reflection", "distance"]
                }
            ]
        }
    ]

    qb[(9, "Chemistry")] = [
        {
            "topic": "Matter in Our Surroundings & Evaporation",
            "questions": [
                {
                    "id": "q1",
                    "text": "Define Evaporation. Explain four factors affecting evaporation with examples.",
                    "marks": 5,
                    "exemplar": "Evaporation is liquid turning to vapor below boiling point. Factors: surface area, temperature, humidity, wind speed.",
                    "avg_ans": "Evaporation is liquid turning into vapor below boiling point. Faster with larger area, higher temperature, lower humidity, and higher wind speed.",
                    "keywords": ["evaporation", "surface", "temperature", "humidity", "wind", "vapor", "liquid", "cooling", "area"]
                },
                {
                    "id": "q2",
                    "text": "What is Latent Heat of Vaporization? Why does steam burn worse than boiling water?",
                    "marks": 4,
                    "exemplar": "Latent heat of vaporization is heat required to change 1 kg liquid to gas without temp change. Steam contains extra latent heat released on skin.",
                    "avg_ans": "Latent heat is heat to turn liquid to gas without temp rise. Steam has extra latent heat of 22.5 * 10^5 J/kg causing worse burns.",
                    "keywords": ["latent", "heat", "vaporization", "steam", "burn", "energy", "boiling", "extra", "joules"]
                },
                {
                    "id": "q3",
                    "text": "Differentiate between Boiling and Evaporation on any three parameters.",
                    "marks": 3,
                    "exemplar": "Evaporation is surface phenomenon below boiling point causing cooling; boiling is bulk phenomenon at boiling point.",
                    "avg_ans": "Evaporation happens at any temp below boiling point and causes cooling. Boiling is a bulk phenomenon at fixed boiling point.",
                    "keywords": ["surface", "bulk", "boiling", "temperature", "cooling", "bubble", "point", "phenomenon"]
                },
                {
                    "id": "q4",
                    "text": "Convert 25°C to Kelvin and 373 K to Celsius. State the formula used.",
                    "marks": 3,
                    "exemplar": "T(K) = T(°C) + 273. 25°C = 298 K. 373 K = 100°C.",
                    "avg_ans": "K = C + 273. 25 C = 298 K. 373 K = 100 C.",
                    "keywords": ["273", "298", "100", "kelvin", "celsius", "k = c", "formula"]
                },
                {
                    "id": "q5",
                    "text": "Why is ice at 273 K more effective in cooling than water at the same temperature?",
                    "marks": 5,
                    "exemplar": "Ice at 273 K absorbs latent heat of fusion (3.34x10^5 J/kg) to melt, extracting more heat than water at 0°C.",
                    "avg_ans": "Ice absorbs extra latent heat of fusion from substance to melt into water, so it cools better than water at 0 C.",
                    "keywords": ["latent", "fusion", "ice", "absorb", "heat", "melt", "energy", "273", "effective"]
                }
            ]
        },
        {
            "topic": "Solutions, Colloids, Suspensions & Tyndall Effect",
            "questions": [
                {
                    "id": "q1",
                    "text": "Differentiate between True Solution, Colloid, and Suspension on particle size, stability, and filterability.",
                    "marks": 5,
                    "exemplar": "1) True Solution: Particle size < 1 nm, completely stable, passes through filter paper (e.g. salt in water). 2) Colloid: Particle size 1 to 100 nm, stable, passes through normal filter paper but scatters light (e.g. milk). 3) Suspension: Particle size > 100 nm, unstable, particles settle down and are caught by filter paper (e.g. chalk in water).",
                    "avg_ans": "True solution has particles < 1nm and is stable. Colloid is between 1-100nm and shows Tyndall effect. Suspension has particles > 100nm and settles down.",
                    "keywords": ["true solution", "colloid", "suspension", "particle size", "1 nm", "100 nm", "stability", "tyndall", "filter"]
                },
                {
                    "id": "q2",
                    "text": "A solution contains 40 g of common salt in 320 g of water. Calculate the concentration in mass percentage.",
                    "marks": 4,
                    "exemplar": "Mass of solute (salt) = 40 g. Mass of solvent (water) = 320 g. Mass of solution = 40 + 320 = 360 g. Concentration = (Mass of solute / Mass of solution) × 100 = (40 / 360) × 100 = 11.11%.",
                    "avg_ans": "Mass of solution = 40 + 320 = 360 g. Mass % = (40 / 360) * 100 = 11.11%.",
                    "keywords": ["11.11%", "11.1%", "360 g", "40", "320", "mass percentage", "solute", "solution"]
                },
                {
                    "id": "q3",
                    "text": "What is the Tyndall Effect? Give two examples from daily life where it is observed.",
                    "marks": 3,
                    "exemplar": "The Tyndall effect is the scattering of a beam of light by colloidal particles in its path, making the light path visible. Examples: 1) Sunlight passing through a dense forest canopy through mist droplets, 2) Light beam from projector in a dusty movie theater.",
                    "avg_ans": "Tyndall effect is scattering of light by colloidal particles. Observed when sunlight enters a dark dusty room or in a dense forest canopy.",
                    "keywords": ["tyndall effect", "scattering", "colloidal", "light path", "canopy", "dusty room", "visible"]
                },
                {
                    "id": "q4",
                    "text": "Classify the following as physical or chemical changes: (i) Rusting of iron, (ii) Melting of ice, (iii) Digestion of food, (iv) Burning of LPG.",
                    "marks": 4,
                    "exemplar": "(i) Rusting of iron: Chemical change (new substance iron oxide formed). (ii) Melting of ice: Physical change (reversible change of state). (iii) Digestion of food: Chemical change (enzymes break down macromolecules permanently). (iv) Burning of LPG: Chemical change (combustion produces CO₂ and H₂O).",
                    "avg_ans": "Rusting is chemical. Melting of ice is physical. Digestion is chemical. Burning of LPG is chemical.",
                    "keywords": ["rusting is chemical", "melting is physical", "digestion is chemical", "burning is chemical", "physical change", "chemical change"]
                },
                {
                    "id": "q5",
                    "text": "What is Chromatography? Explain its operating principle and two applications.",
                    "marks": 4,
                    "exemplar": "Chromatography is a technique used to separate solutes that dissolve in the same solvent. Principle: Differential rates of migration; components with higher solubility in the mobile phase rise faster on the stationary filter paper. Applications: 1) Separating dyes in black ink, 2) Detecting drugs in blood samples.",
                    "avg_ans": "Chromatography separates solutes based on different solubilities in solvent. Used to separate ink dyes and drugs in blood.",
                    "keywords": ["chromatography", "solubility", "separate", "dyes", "ink", "drugs", "blood", "stationary phase"]
                }
            ]
        },
        {
            "topic": "Atoms, Molecules, Valency & Chemical Formulae",
            "questions": [
                {
                    "id": "q1",
                    "text": "State the Law of Conservation of Mass and the Law of Constant Proportions with chemical examples.",
                    "marks": 5,
                    "exemplar": "Law of Conservation of Mass: Mass can neither be created nor destroyed in a chemical reaction (e.g. 12g C + 32g O₂ = 44g CO₂). Law of Constant Proportions: In a chemical compound, elements are always present in definite proportions by mass (e.g. in pure water H₂O, hydrogen and oxygen are always in 1:8 mass ratio).",
                    "avg_ans": "Conservation of mass means total mass of reactants equals products. Constant proportions means elements combine in fixed ratio like water is always 1:8 by mass.",
                    "keywords": ["conservation of mass", "constant proportions", "mass ratio", "1:8", "water", "neither created nor destroyed"]
                },
                {
                    "id": "q2",
                    "text": "Write the chemical formulae by criss-cross method: (a) Aluminium oxide, (b) Calcium chloride, (c) Sodium carbonate.",
                    "marks": 4,
                    "exemplar": "(a) Aluminium oxide: Al³⁺ and O²⁻ -> Al₂O₃. (b) Calcium chloride: Ca²⁺ and Cl⁻ -> CaCl₂. (c) Sodium carbonate: Na⁺ and CO₃²⁻ -> Na₂CO₃.",
                    "avg_ans": "Aluminium oxide = Al2O3. Calcium chloride = CaCl2. Sodium carbonate = Na2CO3.",
                    "keywords": ["al2o3", "cacl2", "na2co3", "criss-cross", "valency"]
                },
                {
                    "id": "q3",
                    "text": "Calculate the molecular mass of: (a) Nitric acid (HNO₃), (b) Glucose (C₆H₁₂O₆). (H=1, N=14, O=16, C=12 u).",
                    "marks": 4,
                    "exemplar": "(a) HNO₃: 1(1) + 1(14) + 3(16) = 1 + 14 + 48 = 63 u. (b) C₆H₁₂O₆: 6(12) + 12(1) + 6(16) = 72 + 12 + 96 = 180 u.",
                    "avg_ans": "HNO3 = 1 + 14 + 48 = 63 u. Glucose = 72 + 12 + 96 = 180 u.",
                    "keywords": ["63 u", "63", "180 u", "180", "molecular mass", "glucose", "hno3"]
                },
                {
                    "id": "q4",
                    "text": "What is an Polyatomic Ion? Give two examples with their chemical formulas and charges.",
                    "marks": 3,
                    "exemplar": "A polyatomic ion is a tightly bound group of atoms that has a net positive or negative electric charge and acts as a single unit in reactions. Examples: Sulfate ion (SO₄²⁻), Ammonium ion (NH₄⁺), Carbonate ion (CO₃²⁻).",
                    "avg_ans": "Group of atoms carrying a charge is polyatomic ion. Examples: NH4+ and SO4 2-.",
                    "keywords": ["polyatomic ion", "group of atoms", "net charge", "so4", "nh4", "ammonium", "sulfate"]
                },
                {
                    "id": "q5",
                    "text": "Define a Mole. Calculate the number of moles in 52 g of Helium gas (Atomic mass of He = 4 u).",
                    "marks": 4,
                    "exemplar": "A mole is the amount of substance containing 6.022 × 10²³ particles (Avogadro's number). Moles = Given mass / Molar mass = 52 g / 4 g/mol = 13 moles.",
                    "avg_ans": "Mole is 6.022 * 10^23 particles. Moles of He = 52 / 4 = 13 moles.",
                    "keywords": ["13 moles", "13", "avogadro", "6.022", "10^23", "52 / 4", "molar mass"]
                }
            ]
        }
    ]

    qb[(9, "Mathematics")] = [
        {
            "topic": "Number Systems, Rationalization & Real Numbers",
            "questions": [
                {
                    "id": "q1",
                    "text": "Show that 0.3333... can be expressed in the form p/q where p, q are integers and q ≠ 0.",
                    "marks": 3,
                    "exemplar": "Let x = 0.333... 10x = 3.333... Subtract: 9x = 3 => x = 1/3.",
                    "avg_ans": "Let x = 0.333... 10x = 3.333... 9x = 3 so x = 3/9 = 1/3.",
                    "keywords": ["1/3", "3/9", "10x", "9x", "p/q", "fraction", "subtract", "let x", "equation", "0.333"]
                },
                {
                    "id": "q2",
                    "text": "Rationalize the denominator of 1 / (7 + 3√2). Show intermediate steps.",
                    "marks": 3,
                    "exemplar": "Multiply conjugate (7 - 3√2) / (49 - 18) = (7 - 3√2) / 31.",
                    "avg_ans": "Multiply top and bottom by (7 - 3√2): (7 - 3√2) / (49 - 18) = (7 - 3√2) / 31.",
                    "keywords": ["7 - 3", "conjugate", "31", "multiply", "denominator", "square", "49 - 18", "rationalize"]
                },
                {
                    "id": "q3",
                    "text": "Find three rational numbers between 3/5 and 4/5.",
                    "marks": 4,
                    "exemplar": "3/5 = 30/50, 4/5 = 40/50. Numbers: 31/50, 32/50, 33/50.",
                    "avg_ans": "Multiply by 10/10: 30/50 and 40/50. Three rational numbers are 31/50, 32/50, 33/50.",
                    "keywords": ["30/50", "40/50", "31/50", "32/50", "33/50", "multiply", "between", "rational", "numbers"]
                },
                {
                    "id": "q4",
                    "text": "Simplify using laws of exponents: (a) 2^(2/3)*2^(1/3), (b) (1/3^3)^7.",
                    "marks": 5,
                    "exemplar": "2^(2/3+1/3) = 2^1 = 2. (3^-3)^7 = 1/3^21.",
                    "avg_ans": "2^(2/3 + 1/3) = 2^1 = 2. (1/3^3)^7 = 1/3^21 = 3^-21.",
                    "keywords": ["2^(2/3", "2^1", "= 2", "3^21", "exponents", "laws"]
                },
                {
                    "id": "q5",
                    "text": "Classify as rational or irrational with justification: (i) 2 - √5, (ii) 2π.",
                    "marks": 5,
                    "exemplar": "2 - √5 is irrational (rational minus irrational). 2π is irrational.",
                    "avg_ans": "2 - √5 is irrational because √5 is irrational. 2π is irrational because π is irrational.",
                    "keywords": ["irrational", "rational", "root 5", "pi", "justification"]
                }
            ]
        },
        {
            "topic": "Polynomials, Remainder Theorem & Factorisation",
            "questions": [
                {
                    "id": "q1",
                    "text": "Factorise by splitting the middle term: 12x² - 7x + 1. Verify using factor theorem.",
                    "marks": 5,
                    "exemplar": "Product = 12 × 1 = 12. Factors summing to -7 are -3 and -4. 12x² - 4x - 3x + 1 = 4x(3x - 1) - 1(3x - 1) = (3x - 1)(4x - 1). Check roots x=1/3 and x=1/4 make polynomial zero.",
                    "avg_ans": "12x² - 4x - 3x + 1 = 4x(3x - 1) - 1(3x - 1) = (3x - 1)(4x - 1).",
                    "keywords": ["(3x - 1)", "(4x - 1)", "splitting middle term", "12", "-3", "-4", "factorise"]
                },
                {
                    "id": "q2",
                    "text": "Evaluate using suitable algebraic identities without direct multiplication: (a) (102)³, (b) (999)².",
                    "marks": 4,
                    "exemplar": "(a) (100 + 2)³ = 100³ + 2³ + 3(100)(2)(100 + 2) = 1,000,000 + 8 + 61,200 = 1,061,208. (b) (1000 - 1)² = 1,000,000 - 2000 + 1 = 998,001.",
                    "avg_ans": "(a) (100+2)³ = 1061208. (b) (1000-1)² = 998001.",
                    "keywords": ["1061208", "998001", "identity", "(a+b)³", "(a-b)²"]
                },
                {
                    "id": "q3",
                    "text": "If x + y + z = 0, prove that x³ + y³ + z³ = 3xyz using algebraic identities.",
                    "marks": 4,
                    "exemplar": "We know identity: x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx). Since x + y + z = 0, RHS = 0 × (...) = 0. Therefore, x³ + y³ + z³ = 3xyz.",
                    "avg_ans": "Identity is x³ + y³ + z³ - 3xyz = (x+y+z)(x²+y²+z²-xy-yz-zx). Since (x+y+z)=0, RHS is 0. So x³+y³+z³ = 3xyz.",
                    "keywords": ["3xyz", "x + y + z = 0", "identity", "rhs = 0", "proved"]
                },
                {
                    "id": "q4",
                    "text": "Find the value of k if (x - 1) is a factor of polynomial p(x) = 2x² + kx + √2.",
                    "marks": 3,
                    "exemplar": "By factor theorem, if (x - 1) is a factor, p(1) = 0. p(1) = 2(1)² + k(1) + √2 = 2 + k + √2 = 0 => k = -(2 + √2).",
                    "avg_ans": "p(1) = 0 => 2(1) + k + √2 = 0 => k = -(2 + √2).",
                    "keywords": ["-(2 + √2)", "-2 - √2", "p(1) = 0", "factor theorem", "k ="]
                },
                {
                    "id": "q5",
                    "text": "Factorise completely: x³ - 23x² + 142x - 120. Show all steps.",
                    "marks": 4,
                    "exemplar": "Check p(1) = 1 - 23 + 142 - 120 = 0, so (x - 1) is a factor. Divide by (x - 1): x³ - 23x² + 142x - 120 = (x - 1)(x² - 22x + 120). Splitting middle term: x² - 12x - 10x + 120 = (x - 12)(x - 10). Factors: (x - 1)(x - 10)(x - 12).",
                    "avg_ans": "p(1)=0 so (x-1) is factor. Dividing gives x² - 22x + 120 = (x-10)(x-12). Answer: (x-1)(x-10)(x-12).",
                    "keywords": ["(x - 1)", "(x - 10)", "(x - 12)", "factorise", "cubic"]
                }
            ]
        },
        {
            "topic": "Linear Equations in Two Variables & Coordinate Geometry",
            "questions": [
                {
                    "id": "q1",
                    "text": "Draw the graph of linear equation 2x + y = 6. Find coordinates of points where it intersects x-axis and y-axis.",
                    "marks": 5,
                    "exemplar": "For x = 0: y = 6 -> (0, 6). For y = 0: 2x = 6 => x = 3 -> (3, 0). For x = 1: y = 4 -> (1, 4). The line passes through (0, 6) and (3, 0), intersecting y-axis at (0, 6) and x-axis at (3, 0).",
                    "avg_ans": "When x=0, y=6 => (0,6). When y=0, x=3 => (3,0). Graph is straight line intersecting axes at (3,0) and (0,6).",
                    "keywords": ["(3, 0)", "(0, 6)", "x-axis", "y-axis", "linear equation", "graph", "coordinates"]
                },
                {
                    "id": "q2",
                    "text": "The taxi fare in a city is ₹8 for the first km and ₹5 per km for subsequent distance. Write a linear equation and find fare for 15 km.",
                    "marks": 4,
                    "exemplar": "Let distance = x km, total fare = ₹y. For first km fare is ₹8, remaining distance is (x - 1) km at ₹5. Equation: y = 8 + 5(x - 1) => y = 5x + 3. For x = 15 km: y = 5(15) + 3 = 75 + 3 = ₹78.",
                    "avg_ans": "Equation: y = 8 + 5(x - 1) => y = 5x + 3. For 15 km: y = 5(15) + 3 = ₹78.",
                    "keywords": ["y = 5x + 3", "78", "₹78", "fare", "taxi fare", "linear equation"]
                },
                {
                    "id": "q3",
                    "text": "State the quadrant or axis for each point: P(-3, 5), Q(4, -2), R(-2, -6), S(0, -4), T(5, 0).",
                    "marks": 3,
                    "exemplar": "P(-3, 5): Quadrant II (- , +). Q(4, -2): Quadrant IV (+ , -). R(-2, -6): Quadrant III (- , -). S(0, -4): Negative y-axis. T(5, 0): Positive x-axis.",
                    "avg_ans": "P is in Quadrant II. Q is in Quadrant IV. R is in Quadrant III. S is on y-axis. T is on x-axis.",
                    "keywords": ["quadrant ii", "quadrant iv", "quadrant iii", "y-axis", "x-axis", "quadrant"]
                },
                {
                    "id": "q4",
                    "text": "Find the value of k if x = 2, y = 1 is a solution of the equation 2x + 3y = k.",
                    "marks": 4,
                    "exemplar": "Substitute x = 2 and y = 1 into the equation: 2(2) + 3(1) = k => 4 + 3 = k => k = 7.",
                    "avg_ans": "Substitute x=2, y=1: 2(2) + 3(1) = 4 + 3 = 7. So k = 7.",
                    "keywords": ["k = 7", "7", "substitute", "solution"]
                },
                {
                    "id": "q5",
                    "text": "Define Cartesian plane, origin, abscissa, and ordinate with coordinate notation.",
                    "marks": 4,
                    "exemplar": "The Cartesian plane is formed by two perpendicular number lines (x-axis and y-axis) intersecting at (0, 0) called Origin. The x-coordinate of a point is its Abscissa (distance from y-axis). The y-coordinate is its Ordinate (distance from x-axis). Notation is (x, y).",
                    "avg_ans": "Cartesian plane has x and y axes meeting at origin (0,0). Abscissa is x-coordinate and Ordinate is y-coordinate.",
                    "keywords": ["cartesian", "origin", "abscissa", "ordinate", "x-axis", "y-axis", "(0, 0)"]
                }
            ]
        }
    ]

    # =========================================================================
    # CLASS 10
    # =========================================================================
    qb[(10, "Physics")] = [
        {
            "topic": "Light - Reflection, Refraction & Lens Formula",
            "questions": [
                {
                    "id": "q1",
                    "text": "State the Laws of Refraction of light. Define Snell's Law and absolute refractive index.",
                    "marks": 5,
                    "exemplar": "1) The incident ray, refracted ray, and normal at the point of incidence all lie in the same plane. 2) Snell's Law: The ratio of sine of angle of incidence to sine of angle of refraction is constant for a given pair of media: sin i / sin r = n. Absolute refractive index n = c / v (speed of light in vacuum / speed in medium).",
                    "avg_ans": "1) Incident, refracted ray and normal lie in same plane. 2) Snell's law: sin i / sin r = constant. Refractive index n = c / v.",
                    "keywords": ["snell's law", "sin i / sin r", "refractive index", "speed of light", "same plane", "laws of refraction"]
                },
                {
                    "id": "q2",
                    "text": "A concave mirror produces a real image 3 times magnified of an object placed 10 cm in front of it. Where is the image located?",
                    "marks": 4,
                    "exemplar": "Object distance u = -10 cm. Magnification m = -3 (real and inverted). Formula: m = -v / u => -3 = -v / (-10) => v = -30 cm. The image is formed at 30 cm in front of the concave mirror.",
                    "avg_ans": "m = -3, u = -10. m = -v/u => -3 = -v/(-10) => v = -30 cm. Image is 30 cm in front of mirror.",
                    "keywords": ["-30 cm", "30 cm", "magnification", "m = -v/u", "concave mirror", "-10"]
                },
                {
                    "id": "q3",
                    "text": "Define Power of a Lens. An optician prescribes a corrective lens of power -2.0 D. Find its focal length and lens type.",
                    "marks": 3,
                    "exemplar": "Power of lens is reciprocal of focal length in metres (P = 1/f). Given P = -2.0 D => f = 1 / P = 1 / (-2.0) = -0.5 m = -50 cm. Since focal length is negative, it is a Concave (diverging) lens used to correct Myopia (nearsightedness).",
                    "avg_ans": "Power P = 1/f. f = 1/-2 = -0.5 m = -50 cm. Negative focal length means concave lens for myopia.",
                    "keywords": ["power", "-0.5 m", "-50 cm", "concave", "myopia", "dioptre", "p = 1/f"]
                },
                {
                    "id": "q4",
                    "text": "Draw/Describe ray diagrams for image formed by convex lens when object is: (a) at 2F1, (b) between F1 and optical center O.",
                    "marks": 4,
                    "exemplar": "(a) At 2F1: Real, inverted image formed at 2F2, same size as object. (b) Between F1 and O: Virtual, erect, magnified image formed on the same side as object (magnifying glass principle).",
                    "avg_ans": "(a) At 2F1: Image at 2F2, real, inverted, same size. (b) Between F1 and O: Virtual, erect, enlarged on same side.",
                    "keywords": ["2f2", "real and inverted", "virtual and erect", "magnified", "convex lens", "same size"]
                },
                {
                    "id": "q5",
                    "text": "Why do stars twinkle in the night sky while planets do not twinkle? Explain atmospheric refraction.",
                    "marks": 4,
                    "exemplar": "Stars are point-sized distant sources. Starlight travels through atmosphere whose optical density continuously fluctuates due to temperature and air currents. The apparent position and intensity of light entering the eye fluctuates, causing twinkling. Planets are closer extended sources; fluctuations from millions of points average out to zero.",
                    "avg_ans": "Stars are point sources and light bends through varying atmosphere layers causing twinkling. Planets are extended sources closer to earth so effect cancels out.",
                    "keywords": ["atmospheric refraction", "point source", "extended source", "twinkle", "cancels out", "density fluctuation"]
                }
            ]
        },
        {
            "topic": "Electricity, Circuits, Ohm's Law & Joule's Heating",
            "questions": [
                {
                    "id": "q1",
                    "text": "State Ohm's Law. Draw circuit diagram to verify it and sketch the V-I characteristic graph.",
                    "marks": 5,
                    "exemplar": "Ohm's Law: Electric current flowing through a metallic conductor is directly proportional to potential difference across its ends, provided temperature remains constant: V = IR. Circuit: Ammeter in series, voltmeter in parallel across resistor, battery, rheostat, and key. V-I graph is a straight line passing through origin.",
                    "avg_ans": "V is proportional to I at constant temperature, V = IR. Straight line graph passing through origin.",
                    "keywords": ["ohm's law", "v = ir", "directly proportional", "straight line", "ammeter", "voltmeter", "constant temperature"]
                },
                {
                    "id": "q2",
                    "text": "Three resistors of 2 Ω, 3 Ω, and 6 Ω are given. (a) Find maximum resistance, (b) Find minimum resistance.",
                    "marks": 4,
                    "exemplar": "(a) Maximum resistance in series: R_max = R1 + R2 + R3 = 2 + 3 + 6 = 11 Ω. (b) Minimum resistance in parallel: 1/R_min = 1/2 + 1/3 + 1/6 = (3 + 2 + 1)/6 = 6/6 = 1 => R_min = 1 Ω.",
                    "avg_ans": "(a) Series gives max: 2 + 3 + 6 = 11 ohms. (b) Parallel gives min: 1/2 + 1/3 + 1/6 = 1 ohm.",
                    "keywords": ["11", "11 ohm", "1 ohm", "1", "series", "parallel", "maximum", "minimum"]
                },
                {
                    "id": "q3",
                    "text": "State Joule's Law of Heating. An electric iron of 1000 W works on 220 V. Calculate current and resistance.",
                    "marks": 4,
                    "exemplar": "Joule's Law: Heat produced H = I²Rt. Power P = V × I => Current I = P / V = 1000 / 220 = 4.55 A. Resistance R = V² / P = 220² / 1000 = 48400 / 1000 = 48.4 Ω.",
                    "avg_ans": "H = I²Rt. Current I = 1000/220 = 4.55 A. Resistance R = 220²/1000 = 48.4 ohms.",
                    "keywords": ["joule's law", "h = i²rt", "4.55 a", "48.4", "ohms", "power", "current"]
                },
                {
                    "id": "q4",
                    "text": "Why are alloys like Nichrome used as heating elements in electric toasters instead of pure copper?",
                    "marks": 3,
                    "exemplar": "1) Nichrome has much higher electrical resistivity than pure copper, producing substantial heat (H ∝ R). 2) Nichrome does not oxidize (burn) even at red-hot high temperatures (high melting point).",
                    "avg_ans": "Nichrome has high resistivity and does not oxidize or melt at high temperatures.",
                    "keywords": ["nichrome", "resistivity", "oxidize", "melting point", "heating element"]
                },
                {
                    "id": "q5",
                    "text": "What is an electric fuse? On which effect of current does it work and why is it connected in the live wire?",
                    "marks": 4,
                    "exemplar": "An electric fuse is a safety device containing a low-melting-point wire that protects appliances from overloading/short-circuiting. It works on the heating effect of electric current. It is connected in the live wire so that when it melts, the high-voltage supply is completely disconnected from the appliance.",
                    "avg_ans": "Safety device with low melting point wire working on heating effect. Connected in live wire to disconnect high voltage during fault.",
                    "keywords": ["fuse", "safety device", "low melting point", "heating effect", "live wire", "overloading", "short-circuit"]
                }
            ]
        },
        {
            "topic": "Magnetic Effects of Electric Current & Solenoids",
            "questions": [
                {
                    "id": "q1",
                    "text": "What is a Solenoid? Describe the magnetic field pattern inside and outside a current-carrying solenoid.",
                    "marks": 5,
                    "exemplar": "A solenoid is a long coil containing many circular turns of insulated copper wire wrapped closely in cylindrical form. Inside the solenoid, magnetic field lines are parallel and straight, indicating a uniform magnetic field. Outside, it forms loops identical to a bar magnet with North and South poles.",
                    "avg_ans": "Coil of insulated copper wire in cylinder. Inside field is uniform and parallel. Outside field resembles a bar magnet.",
                    "keywords": ["solenoid", "coil", "uniform", "parallel lines", "bar magnet", "north and south", "magnetic field"]
                },
                {
                    "id": "q2",
                    "text": "State Fleming's Left-Hand Rule. Name an appliance that operates on this principle.",
                    "marks": 4,
                    "exemplar": "Stretch thumb, forefinger, and middle finger mutually perpendicular: Forefinger points in direction of Magnetic field, Middle finger in direction of Current, then Thumb points in direction of Force/Motion. Appliance: Electric Motor.",
                    "avg_ans": "Thumb = Force, Forefinger = Magnetic Field, Middle finger = Current when perpendicular. Used in electric motors.",
                    "keywords": ["fleming's left-hand", "thumb", "forefinger", "middle finger", "force", "field", "current", "electric motor"]
                },
                {
                    "id": "q3",
                    "text": "What is Electromagnetic Induction? State Fleming's Right-Hand Rule.",
                    "marks": 4,
                    "exemplar": "Electromagnetic Induction is generation of induced electric current in a conductor due to a changing magnetic field. Fleming's Right-Hand Rule: Stretch thumb (Motion of conductor), forefinger (Magnetic Field), then middle finger points in direction of Induced Current.",
                    "avg_ans": "Generating induced current by changing magnetic field. Thumb is motion, forefinger is field, middle finger is induced current.",
                    "keywords": ["electromagnetic induction", "induced current", "changing magnetic field", "fleming's right-hand", "generator"]
                },
                {
                    "id": "q4",
                    "text": "Why do two magnetic field lines never intersect each other? Explain with compass needle.",
                    "marks": 3,
                    "exemplar": "If two field lines intersected, at the point of intersection a magnetic compass needle would have to point in two different directions simultaneously, which is physically impossible. Hence lines never intersect.",
                    "avg_ans": "If they intersect, compass needle would point in two directions at the same point, which is impossible.",
                    "keywords": ["never intersect", "two directions", "compass needle", "impossible", "tangent"]
                },
                {
                    "id": "q5",
                    "text": "Differentiate between Overloading and Short-Circuiting in domestic circuits. What is the role of Earth wire?",
                    "marks": 4,
                    "exemplar": "Short-circuiting occurs when live and neutral wires touch directly due to faulty insulation, dropping resistance to zero and causing huge current surge. Overloading occurs when too many appliances are turned on simultaneously, exceeding current capacity. Earth wire provides a low-resistance path to ground, safely conducting leakage current without shock.",
                    "avg_ans": "Short circuit is live and neutral wire touching. Overloading is too many appliances drawing current. Earth wire carries leakage to ground preventing electric shock.",
                    "keywords": ["short-circuiting", "overloading", "live and neutral", "earth wire", "electric shock", "leakage"]
                }
            ]
        }
    ]

    qb[(10, "Chemistry")] = [
        {
            "topic": "Chemical Reactions, Balancing & Types of Reactions",
            "questions": [
                {
                    "id": "q1",
                    "text": "Balance the chemical equation: Fe + H₂O → Fe₃O₄ + H₂. Why must chemical equations be balanced?",
                    "marks": 5,
                    "exemplar": "Balanced Equation: 3Fe + 4H₂O → Fe₃O₄ + 4H₂. Equations must be balanced to satisfy the Law of Conservation of Mass; total number of atoms of each element on reactant side must equal product side.",
                    "avg_ans": "3Fe + 4H2O -> Fe3O4 + 4H2. Balanced to follow law of conservation of mass so atoms on both sides are equal.",
                    "keywords": ["3fe + 4h2o", "fe3o4 + 4h2", "balanced", "conservation of mass", "atoms equal"]
                },
                {
                    "id": "q2",
                    "text": "Differentiate between Displacement and Double Displacement reactions with balanced chemical equations.",
                    "marks": 4,
                    "exemplar": "Displacement: A more reactive element displaces a less reactive element from its salt solution (e.g. Fe + CuSO₄ → FeSO₄ + Cu). Double Displacement: Two compounds exchange ions to form two new compounds, often forming a precipitate (e.g. Na₂SO₄ + BaCl₂ → BaSO₄↓ + 2NaCl).",
                    "avg_ans": "Displacement: more reactive replaces less reactive (Fe + CuSO4 -> FeSO4 + Cu). Double displacement: exchange of ions (Na2SO4 + BaCl2 -> BaSO4 + 2NaCl).",
                    "keywords": ["displacement", "double displacement", "cuso4", "bacl2", "baso4", "exchange ions", "precipitate"]
                },
                {
                    "id": "q3",
                    "text": "What is a Redox Reaction? In CuO + H₂ → Cu + H₂O, identify substance oxidized, reduced, oxidizing agent, and reducing agent.",
                    "marks": 4,
                    "exemplar": "Redox reaction involves simultaneous oxidation (gain of oxygen/loss of electrons) and reduction (loss of oxygen/gain of electrons). Substance oxidized: H₂ (gains oxygen). Substance reduced: CuO (loses oxygen). Oxidizing agent: CuO. Reducing agent: H₂.",
                    "avg_ans": "Redox has oxidation and reduction together. Oxidized: H2. Reduced: CuO. Oxidizing agent: CuO. Reducing agent: H2.",
                    "keywords": ["redox", "oxidized: h2", "reduced: cuo", "oxidizing agent: cuo", "reducing agent: h2", "oxygen"]
                },
                {
                    "id": "q4",
                    "text": "Why does the blue color of copper sulphate solution fade and iron nail becomes brownish when placed in it?",
                    "marks": 3,
                    "exemplar": "Iron is more reactive than copper in the reactivity series. Iron displaces copper: Fe + CuSO₄ (blue) → FeSO₄ (pale green) + Cu (brownish deposit on nail). Hence blue color fades as green ferrous sulphate forms.",
                    "avg_ans": "Iron displaces copper from CuSO4 solution because iron is more reactive. Blue CuSO4 becomes pale green FeSO4 and reddish-brown copper deposits on nail.",
                    "keywords": ["iron is more reactive", "displaces copper", "feso4", "green", "brown deposit", "reactivity series"]
                },
                {
                    "id": "q5",
                    "text": "What is Rancidity? State two methods commonly used in food packaging to prevent rancidity.",
                    "marks": 4,
                    "exemplar": "Rancidity is the slow oxidation of fats and oils in food, producing unpleasant smell and taste. Prevention methods: 1) Flushing chips packets with unreactive Nitrogen gas to prevent oxygen contact, 2) Adding antioxidants like BHA/BHT, 3) Refrigeration in airtight containers.",
                    "avg_ans": "Rancidity is oxidation of fats and oils making food smell bad. Prevented by flushing with nitrogen gas and using airtight containers with antioxidants.",
                    "keywords": ["rancidity", "oxidation", "fats and oils", "nitrogen gas", "antioxidants", "airtight", "smell and taste"]
                }
            ]
        },
        {
            "topic": "Acids, Bases, pH Scale & Important Salts",
            "questions": [
                {
                    "id": "q1",
                    "text": "What is the pH scale? Explain the role of pH in: (a) human digestive system, (b) prevention of tooth decay.",
                    "marks": 5,
                    "exemplar": "pH measures hydrogen ion concentration (0-14, <7 acidic, 7 neutral, >7 basic). (a) Stomach produces HCl (pH ~1.2) for pepsin enzyme; excess acid causes acidity treated with antacids like Mg(OH)₂. (b) Tooth decay starts when mouth pH falls below 5.5 as bacteria produce acids from sugar; toothpaste (basic) neutralizes acid.",
                    "avg_ans": "pH measures H+ ions. Stomach needs pH ~1.5 to digest food, antacid cures acidity. Tooth decay happens below pH 5.5, toothpaste is basic to neutralize it.",
                    "keywords": ["ph scale", "digestive system", "hcl", "tooth decay", "5.5", "antacids", "neutralize", "toothpaste"]
                },
                {
                    "id": "q2",
                    "text": "Write the chemical name, formula, preparation equation, and two uses of Bleaching Powder.",
                    "marks": 4,
                    "exemplar": "Chemical Name: Calcium oxychloride, Formula: CaOCl₂. Preparation: Passing chlorine gas over dry slaked lime: Ca(OH)₂ + Cl₂ → CaOCl₂ + H₂O. Uses: 1) Disinfecting drinking water, 2) Bleaching cotton and linen in textile industry.",
                    "avg_ans": "Calcium oxychloride, CaOCl2. Prepared by Ca(OH)2 + Cl2 -> CaOCl2 + H2O. Used to disinfect water and bleach textiles.",
                    "keywords": ["bleaching powder", "caocl2", "calcium oxychloride", "ca(oh)2 + cl2", "disinfecting water", "textile"]
                },
                {
                    "id": "q3",
                    "text": "What is Plaster of Paris? Write its preparation equation from Gypsum. Why must it be kept in moisture-proof containers?",
                    "marks": 4,
                    "exemplar": "Plaster of Paris is Calcium sulphate hemihydrate: CaSO₄·1/2H₂O. Preparation by heating Gypsum at 373 K: CaSO₄·2H₂O → CaSO₄·1/2H₂O + 1.5H₂O. It must be stored in moisture-proof containers because it absorbs water and sets into hard solid Gypsum.",
                    "avg_ans": "Plaster of Paris is CaSO4.1/2H2O. Made by heating gypsum at 373 K. It absorbs moisture and hardens into gypsum so must be stored dry.",
                    "keywords": ["plaster of paris", "caso4.1/2h2o", "gypsum", "373 k", "moisture-proof", "hardens", "calcium sulphate hemihydrate"]
                },
                {
                    "id": "q4",
                    "text": "Why does dry HCl gas not turn dry blue litmus paper red, whereas aqueous HCl solution turns it red?",
                    "marks": 3,
                    "exemplar": "Acids show acidic properties only in the presence of water, because water is needed to ionize HCl into hydrogen ions (H⁺ or H₃O⁺). Dry HCl gas has no free H⁺ ions, so it does not change dry litmus color.",
                    "avg_ans": "Dry HCl gas has no moisture so no H+ ions are produced. In water it forms H+ (H3O+) ions which turn blue litmus red.",
                    "keywords": ["h+ ions", "h3o+", "water", "ionize", "dry hcl", "no ions", "acidic property"]
                },
                {
                    "id": "q5",
                    "text": "What is Neutralization reaction? Give one balanced equation and explain why baking soda relieves ant stings.",
                    "marks": 4,
                    "exemplar": "Neutralization: Reaction between an acid and a base to form salt and water: HCl + NaOH → NaCl + H₂O. An ant sting injects acidic Methanoic (Formic) acid into the skin. Applying mild basic baking soda (NaHCO₃) neutralizes the acid, relieving burning pain.",
                    "avg_ans": "Acid + Base -> Salt + Water. Ant sting injects formic acid. Baking soda is a base that neutralizes the acid and stops pain.",
                    "keywords": ["neutralization", "acid + base", "methanoic acid", "formic acid", "baking soda", "nahco3", "ant sting"]
                }
            ]
        },
        {
            "topic": "Metals, Reactivity Series & Carbon Compounds",
            "questions": [
                {
                    "id": "q1",
                    "text": "Explain ionic bonding with electron-dot structures for NaCl and MgO. State two properties of ionic compounds.",
                    "marks": 5,
                    "exemplar": "NaCl: Na (2,8,1) loses 1 electron -> Na⁺; Cl (2,8,7) gains 1 electron -> Cl⁻; electrostatic attraction forms NaCl. MgO: Mg (2,8,2) transfers 2 electrons to O (2,6) -> Mg²⁺ + O²⁻ -> MgO. Properties: 1) High melting/boiling points, 2) Conduct electricity in molten/aqueous state.",
                    "avg_ans": "Na transfers 1 electron to Cl forming Na+ and Cl-. Mg transfers 2 electrons to O forming Mg2+ and O2-. High melting point, conducts in molten state.",
                    "keywords": ["ionic bond", "electron-dot", "na+", "cl-", "mg2+", "o2-", "transfer of electrons", "high melting point", "conduct electricity"]
                },
                {
                    "id": "q2",
                    "text": "What is the Reactivity Series? Explain the difference between Roasting and Calcination with chemical equations.",
                    "marks": 4,
                    "exemplar": "Reactivity Series: Arrangement of metals in order of decreasing chemical reactivity. Roasting: Heating sulphide ores in excess air (2ZnS + 3O₂ → 2ZnO + 2SO₂). Calcination: Heating carbonate ores in limited/no air (ZnCO₃ → ZnO + CO₂).",
                    "avg_ans": "Reactivity series lists metals by reactivity. Roasting heats sulphide ore in excess air. Calcination heats carbonate ore in limited air.",
                    "keywords": ["reactivity series", "roasting", "calcination", "zns", "znco3", "excess air", "limited air"]
                },
                {
                    "id": "q3",
                    "text": "Why does carbon form covalent bonds rather than C⁴⁺ or C⁴⁻ ions? Explain Catenation and Tetravalency.",
                    "marks": 4,
                    "exemplar": "Carbon cannot gain 4 electrons to form C⁴⁻ as nucleus (6 protons) cannot hold 10 electrons. It cannot lose 4 electrons to form C⁴⁺ due to massive ionization energy needed. Hence it shares 4 valence electrons (Tetravalency). Catenation is carbon's unique ability to form long stable chains with other carbon atoms.",
                    "avg_ans": "Carbon shares electrons because gaining or losing 4 electrons requires too much energy. Tetravalency is 4 valence electrons. Catenation is self-linking to form long chains.",
                    "keywords": ["covalent bonds", "tetravalency", "catenation", "share electrons", "cannot form c4+", "cannot form c4-", "energy"]
                },
                {
                    "id": "q4",
                    "text": "What is a Homologous Series? State three characteristics and write formulae for the first three Alkanes.",
                    "marks": 4,
                    "exemplar": "A homologous series is a family of organic compounds having the same functional group and similar chemical properties. Characteristics: 1) Successive members differ by -CH₂ unit (14 u mass), 2) Same general formula (CnH2n+2 for alkanes), 3) Gradation in physical properties. Alkanes: Methane (CH₄), Ethane (C₂H₆), Propane (C₃H₈).",
                    "avg_ans": "Series of compounds differing by -CH2 unit. First three alkanes: Methane (CH4), Ethane (C2H6), Propane (C3H8).",
                    "keywords": ["homologous series", "-ch2", "cnh2n+2", "methane ch4", "ethane c2h6", "propane c3h8", "similar chemical properties"]
                },
                {
                    "id": "q5",
                    "text": "Differentiate between Saturated and Unsaturated hydrocarbons using structural formulas and bromine water test.",
                    "marks": 3,
                    "exemplar": "Saturated hydrocarbons have single C-C bonds (alkanes); they do not decolorize brown bromine water. Unsaturated hydrocarbons have double (alkenes) or triple (alkynes) bonds; they rapidly decolorize bromine water due to addition reaction across multiple bonds.",
                    "avg_ans": "Saturated has single bonds and does not decolorize bromine water. Unsaturated has double/triple bonds and decolorizes bromine water.",
                    "keywords": ["saturated", "unsaturated", "single bond", "double bond", "bromine water", "decolorize", "addition reaction"]
                }
            ]
        }
    ]

    qb[(10, "Mathematics")] = [
        {
            "topic": "Real Numbers, Fundamental Theorem of Arithmetic & Polynomials",
            "questions": [
                {
                    "id": "q1",
                    "text": "Prove by contradiction that √5 is an irrational number.",
                    "marks": 5,
                    "exemplar": "Assume √5 is rational: √5 = a/b where a, b are coprime integers. 5 = a²/b² => a² = 5b², so 5 divides a², thus 5 divides a. Let a = 5c => (5c)² = 5b² => 25c² = 5b² => b² = 5c², so 5 divides b. Thus 5 is a common factor of a and b, contradicting that a and b are coprime. Hence √5 is irrational.",
                    "avg_ans": "Assume √5 = a/b coprime. 5b² = a² so 5 divides a. Let a = 5c, then 5c² = b² so 5 divides b. Contradicts coprime assumption. So √5 is irrational.",
                    "keywords": ["contradiction", "coprime", "irrational", "5 divides", "a/b", "root 5", "proved"]
                },
                {
                    "id": "q2",
                    "text": "State the Fundamental Theorem of Arithmetic. Find HCF and LCM of 306 and 657 and verify HCF × LCM = Product.",
                    "marks": 4,
                    "exemplar": "Every composite number can be uniquely expressed as product of primes. 306 = 2 × 3² × 17. 657 = 3² × 73. HCF = 3² = 9. LCM = 2 × 3² × 17 × 73 = 22,338. HCF × LCM = 9 × 22,338 = 201,042. Product = 306 × 657 = 201,042. Verified.",
                    "avg_ans": "HCF = 9, LCM = 22338. 9 * 22338 = 201042 = 306 * 657. Verified.",
                    "keywords": ["fundamental theorem", "hcf = 9", "lcm = 22338", "201042", "verified", "prime factorisation"]
                },
                {
                    "id": "q3",
                    "text": "Find zeroes of quadratic polynomial x² + 7x + 10 and verify relationship between zeroes and coefficients.",
                    "marks": 4,
                    "exemplar": "x² + 7x + 10 = (x + 2)(x + 5) = 0 => zeroes are α = -2, β = -5. Sum of zeroes: α + β = -2 + (-5) = -7 = -b/a = -7/1. Product of zeroes: αβ = (-2)(-5) = 10 = c/a = 10/1. Verified.",
                    "avg_ans": "Zeroes are -2 and -5. Sum = -7 = -b/a. Product = 10 = c/a. Relationship verified.",
                    "keywords": ["-2", "-5", "sum = -7", "product = 10", "-b/a", "c/a", "zeroes", "verified"]
                },
                {
                    "id": "q4",
                    "text": "Find a quadratic polynomial whose sum and product of zeroes are -3 and 2 respectively.",
                    "marks": 3,
                    "exemplar": "Quadratic polynomial formula: p(x) = k[x² - (Sum)x + Product] = k[x² - (-3)x + 2] = k[x² + 3x + 2]. For k = 1, polynomial is x² + 3x + 2.",
                    "avg_ans": "Formula: x² - (sum)x + product = x² - (-3)x + 2 = x² + 3x + 2.",
                    "keywords": ["x² + 3x + 2", "sum of zeroes", "product of zeroes", "-3", "2"]
                },
                {
                    "id": "q5",
                    "text": "Check whether 6ⁿ can end with digit 0 for any natural number n. Justify.",
                    "marks": 4,
                    "exemplar": "A number ends with 0 if its prime factorisation contains both 2 and 5 (2 × 5 = 10). Prime factorisation of 6ⁿ = (2 × 3)ⁿ = 2ⁿ × 3ⁿ. By Fundamental Theorem of Arithmetic, this factorisation is unique and does not contain 5. Hence 6ⁿ can never end with digit 0.",
                    "avg_ans": "To end in 0, prime factors must have 2 and 5. 6ⁿ = (2*3)ⁿ has no factor 5. So it cannot end in 0.",
                    "keywords": ["cannot end with 0", "factor 5", "2 and 5", "prime factorisation", "(2 * 3)ⁿ", "unique"]
                }
            ]
        },
        {
            "topic": "Quadratic Equations & Arithmetic Progressions (AP)",
            "questions": [
                {
                    "id": "q1",
                    "text": "Solve by quadratic formula: 2x² - 7x + 3 = 0. Determine nature of roots using discriminant.",
                    "marks": 5,
                    "exemplar": "a = 2, b = -7, c = 3. Discriminant D = b² - 4ac = (-7)² - 4(2)(3) = 49 - 24 = 25 > 0. Two distinct real roots. x = (-b ± √D)/(2a) = (7 ± 5)/4 => x = 12/4 = 3 or x = 2/4 = 1/2. Roots are 3 and 1/2.",
                    "avg_ans": "D = 49 - 24 = 25 > 0 (two real roots). x = (7 ± 5)/4 => x = 3 and x = 1/2.",
                    "keywords": ["x = 3", "x = 1/2", "discriminant", "d = 25", "quadratic formula", "real roots"]
                },
                {
                    "id": "q2",
                    "text": "Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
                    "marks": 4,
                    "exemplar": "Common difference d = 8 - 3 = 5. Reverse the AP: First term a = 253, d = -5. Formula: a20 = a + (n - 1)d = 253 + (20 - 1)(-5) = 253 + 19(-5) = 253 - 95 = 158.",
                    "avg_ans": "Reversing AP: a = 253, d = -5. a20 = 253 + 19(-5) = 253 - 95 = 158.",
                    "keywords": ["158", "20th term", "from last", "253", "d = -5", "ap"]
                },
                {
                    "id": "q3",
                    "text": "The 4th and 8th terms of an AP sum to 24, and 6th and 10th terms sum to 44. Find the first three terms.",
                    "marks": 4,
                    "exemplar": "a4 + a8 = (a + 3d) + (a + 7d) = 2a + 10d = 24 => a + 5d = 12 (Eq 1). a6 + a10 = (a + 5d) + (a + 9d) = 2a + 14d = 44 => a + 7d = 22 (Eq 2). Subtracting: 2d = 10 => d = 5. From Eq 1: a + 25 = 12 => a = -13. First three terms: -13, -8, -3.",
                    "avg_ans": "a + 5d = 12 and a + 7d = 22 => 2d = 10 => d = 5. a = -13. First three terms are -13, -8, -3.",
                    "keywords": ["-13", "-8", "-3", "d = 5", "a = -13", "ap", "first three terms"]
                },
                {
                    "id": "q4",
                    "text": "For what value of k does the quadratic equation kx(x - 2) + 6 = 0 have two equal real roots?",
                    "marks": 4,
                    "exemplar": "kx² - 2kx + 6 = 0. a = k, b = -2k, c = 6. For equal roots, D = b² - 4ac = 0 => (-2k)² - 4(k)(6) = 0 => 4k² - 24k = 0 => 4k(k - 6) = 0. Since k ≠ 0 for a quadratic equation, k = 6.",
                    "avg_ans": "kx² - 2kx + 6 = 0. Equal roots: b² - 4ac = 0 => 4k² - 24k = 0 => k(k - 6) = 0. k cannot be 0, so k = 6.",
                    "keywords": ["k = 6", "6", "equal roots", "b² - 4ac = 0", "discriminant"]
                },
                {
                    "id": "q5",
                    "text": "How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?",
                    "marks": 3,
                    "exemplar": "a = 9, d = 8, Sn = 636. Sn = n/2 [2a + (n-1)d] => 636 = n/2 [18 + 8n - 8] = n/2 [8n + 10] = n(4n + 5) = 4n² + 5n. 4n² + 5n - 636 = 0 => (4n + 53)(n - 12) = 0. Since n must be positive integer, n = 12 terms.",
                    "avg_ans": "Sn = n/2 [18 + (n-1)8] = 4n² + 5n = 636 => 4n² + 5n - 636 = 0 => (n - 12)(4n + 53) = 0 => n = 12.",
                    "keywords": ["n = 12", "12 terms", "sn = 636", "4n² + 5n - 636", "ap"]
                }
            ]
        },
        {
            "topic": "Triangles (Similarity) & Trigonometric Identities",
            "questions": [
                {
                    "id": "q1",
                    "text": "State and prove Basic Proportionality Theorem (Thales Theorem).",
                    "marks": 5,
                    "exemplar": "Statement: If a line is drawn parallel to one side of a triangle intersecting other two sides, it divides them in the same ratio. In ΔABC, DE || BC. Area(ΔADE) = 1/2 × AD × EN. Area(ΔBDE) = 1/2 × BD × EN. Ratio = AD/BD. Similarly Area(ΔADE)/Area(ΔCDE) = AE/EC. Since ΔBDE and ΔCDE share base DE and lie between same parallels DE and BC, Area(ΔBDE) = Area(ΔCDE). Hence AD/BD = AE/EC.",
                    "avg_ans": "Line parallel to one side divides other two sides in same ratio. AD/DB = AE/EC using area of triangles on same base DE.",
                    "keywords": ["basic proportionality", "thales", "ad/db = ae/ec", "parallel", "ratio", "proved"]
                },
                {
                    "id": "q2",
                    "text": "If tan θ = 4/3, find all other trigonometric ratios (sin θ, cos θ, cot θ, sec θ, cosec θ).",
                    "marks": 4,
                    "exemplar": "tan θ = Opposite / Adjacent = 4/3. Hypotenuse = √(4² + 3²) = 5. Ratios: sin θ = 4/5, cos θ = 3/5, cosec θ = 5/4, sec θ = 5/3, cot θ = 3/4.",
                    "avg_ans": "Hypotenuse = 5. sin θ = 4/5, cos θ = 3/5, cosec θ = 5/4, sec θ = 5/3, cot θ = 3/4.",
                    "keywords": ["sin θ = 4/5", "cos θ = 3/5", "5/4", "5/3", "3/4", "hypotenuse = 5", "trigonometric ratios"]
                },
                {
                    "id": "q3",
                    "text": "Prove the trigonometric identity: (sin A + cosec A)² + (cos A + sec A)² = 7 + tan² A + cot² A.",
                    "marks": 4,
                    "exemplar": "LHS: (sin²A + cosec²A + 2sinA·cosecA) + (cos²A + sec²A + 2cosA·secA). Since sinA·cosecA = 1 and cosA·secA = 1, 2 + 2 = 4. (sin²A + cos²A) = 1. Subtotal = 1 + 4 = 5. Using cosec²A = 1 + cot²A and sec²A = 1 + tan²A: LHS = 5 + (1 + cot²A) + (1 + tan²A) = 7 + tan²A + cot²A = RHS. Proved.",
                    "avg_ans": "Expand squares: sin²A + cos²A + 2(1) + 2(1) + cosec²A + sec²A = 5 + (1 + cot²A) + (1 + tan²A) = 7 + tan²A + cot²A.",
                    "keywords": ["7 + tan²", "cot²", "sin² + cos² = 1", "identity", "proved", "lhs = rhs"]
                },
                {
                    "id": "q4",
                    "text": "Evaluate without using tables: (cos 37° / sin 53°) + (sin 41° / cos 49°).",
                    "marks": 3,
                    "exemplar": "Using complementary angle identities: cos(90° - θ) = sin θ. cos 37° = cos(90° - 53°) = sin 53°. sin 41° = sin(90° - 49°) = cos 49°. Expression = (sin 53° / sin 53°) + (cos 49° / cos 49°) = 1 + 1 = 2.",
                    "avg_ans": "cos 37 = sin 53 and sin 41 = cos 49. Expression = 1 + 1 = 2.",
                    "keywords": ["= 2", "1 + 1", "complementary", "cos(90 - theta)", "sin 53", "cos 49"]
                },
                {
                    "id": "q5",
                    "text": "A ladder 10 m long rests against a vertical wall, reaching a window 8 m above the ground. Find distance of foot of ladder from the wall.",
                    "marks": 4,
                    "exemplar": "Let distance be x m. By Pythagoras theorem in right triangle: Ladder² = Wall² + Distance² => 10² = 8² + x² => 100 = 64 + x² => x² = 36 => x = 6 m. The foot of the ladder is 6 m from the wall.",
                    "avg_ans": "By Pythagoras theorem: x² + 8² = 10² => x² = 100 - 64 = 36 => x = 6 m.",
                    "keywords": ["6 m", "6", "pythagoras", "100 - 64 = 36", "ladder", "wall"]
                }
            ]
        }
    ]

    return qb

def get_question_set(subject: str, student_class: int, custom_topic: str = "", set_index: int = 0):
    """
    Returns a 5-question curriculum set for any class and subject.
    Cycles through available sets when refreshed.
    """
    qb = get_full_question_bank()
    key = (student_class, subject)

    # If user provided a specific custom topic in the open text box
    if custom_topic and len(custom_topic.strip()) > 2:
        topic_clean = custom_topic.strip()
        kw_base = [w.lower() for w in topic_clean.split() if len(w) > 2]
        
        # Multiple sets for custom topic
        custom_variations = [
            {
                "topic_title": f"Custom Mastery: {topic_clean} (Analytical Set A)",
                "questions": [
                    {
                        "id": "q1",
                        "text": f"State the fundamental definition and core governing principles of '{topic_clean}'. Define all scientific terms.",
                        "marks": 5,
                        "exemplar": f"{topic_clean} is a foundational scientific/mathematical concept governing state interactions, physical laws, and quantitative relationships in this domain.",
                        "avg_ans": f"{topic_clean} deals with the fundamental physical and mathematical rules governing this system.",
                        "keywords": kw_base + ["principle", "definition", "law", "system", "formula"]
                    },
                    {
                        "id": "q2",
                        "text": f"Explain a real-world daily-life observation or application that directly demonstrates '{topic_clean}'.",
                        "marks": 4,
                        "exemplar": f"In everyday life, {topic_clean} is demonstrated when energy, forces, or material properties interact under environmental conditions.",
                        "avg_ans": f"We observe {topic_clean} in daily life through practical experiments and natural phenomena.",
                        "keywords": kw_base + ["example", "daily life", "observation", "application"]
                    },
                    {
                        "id": "q3",
                        "text": f"Derive or formulate the key mathematical equation or quantitative relation associated with '{topic_clean}'.",
                        "marks": 4,
                        "exemplar": f"The quantitative behavior of {topic_clean} can be formulated mathematically relating input variables to the resultant magnitude.",
                        "avg_ans": f"The formula for {topic_clean} expresses the direct and inverse proportionalities mathematically.",
                        "keywords": kw_base + ["formula", "equation", "derivation", "relation", "proportional"]
                    },
                    {
                        "id": "q4",
                        "text": f"What are the primary factors that influence the rate or magnitude of '{topic_clean}'? Explain any two.",
                        "marks": 4,
                        "exemplar": f"Key factors affecting {topic_clean} include temperature, applied potential, surface characteristics, and material constants.",
                        "avg_ans": f"Factors affecting {topic_clean} include temperature, medium, and applied force or energy.",
                        "keywords": kw_base + ["factors", "temperature", "magnitude", "rate", "affect"]
                    },
                    {
                        "id": "q5",
                        "text": f"Mention two practical limitations, safety precautions, or industrial utilities of '{topic_clean}'.",
                        "marks": 3,
                        "exemplar": f"Practical applications of {topic_clean} include manufacturing and engineering design, requiring safety controls against excess heat or strain.",
                        "avg_ans": f"Used in industry for product design and requires safety checks to avoid damage.",
                        "keywords": kw_base + ["limitations", "safety", "industry", "precautions", "utility"]
                    }
                ]
            },
            {
                "topic_title": f"Custom Mastery: {topic_clean} (Problem Solving Set B)",
                "questions": [
                    {
                        "id": "q1",
                        "text": f"Explain the step-by-step experimental setup used to verify or study '{topic_clean}' in a standard laboratory.",
                        "marks": 5,
                        "exemplar": f"The standard laboratory apparatus for studying {topic_clean} consists of calibrated sensors, controlled environment, and measuring indicators.",
                        "avg_ans": f"Laboratory setup uses measuring instruments to record changes under controlled conditions.",
                        "keywords": kw_base + ["apparatus", "laboratory", "experiment", "setup", "verify"]
                    },
                    {
                        "id": "q2",
                        "text": f"Differentiate between theoretical predictions and practical observations when analyzing '{topic_clean}'.",
                        "marks": 4,
                        "exemplar": f"Theoretical models of {topic_clean} assume ideal conditions, whereas practical observations involve frictional, resistive, or thermal losses.",
                        "avg_ans": f"Theory assumes no losses while practical experiments have small errors and friction.",
                        "keywords": kw_base + ["theoretical", "practical", "difference", "losses", "ideal"]
                    },
                    {
                        "id": "q3",
                        "text": f"Solve or explain how units and dimensional consistency are maintained when calculating '{topic_clean}'.",
                        "marks": 4,
                        "exemplar": f"Dimensional consistency requires all quantities in {topic_clean} equations to match standard SI base units (kg, m, s, A).",
                        "avg_ans": f"SI units must be converted properly like meters and seconds before calculating {topic_clean}.",
                        "keywords": kw_base + ["units", "si units", "dimensional", "consistency", "calculation"]
                    },
                    {
                        "id": "q4",
                        "text": f"Why is understanding '{topic_clean}' essential in modern technology and scientific development?",
                        "marks": 4,
                        "exemplar": f"Understanding {topic_clean} is critical for advancing energy efficiency, electronic devices, and aerospace systems.",
                        "avg_ans": f"Crucial for modern engineering, electronics and scientific progress.",
                        "keywords": kw_base + ["technology", "development", "modern", "engineering", "importance"]
                    },
                    {
                        "id": "q5",
                        "text": f"Summarize three key takeaways or conclusions about '{topic_clean}' for board examination revision.",
                        "marks": 3,
                        "exemplar": f"Three takeaways: 1) Core definition and SI units, 2) Governing formula and derivations, 3) Real-world applications and graph behaviors.",
                        "avg_ans": f"Key points are definition, formula, and daily life applications.",
                        "keywords": kw_base + ["takeaways", "summary", "conclusion", "revision", "points"]
                    }
                ]
            }
        ]
        
        chosen_var = custom_variations[set_index % len(custom_variations)]
        return {
            "topic_title": chosen_var["topic_title"],
            "questions": chosen_var["questions"],
            "total_sets": len(custom_variations)
        }

    # Standard curriculum bank lookup
    sets = qb.get(key)
    if not sets:
        # Fallback to Class 9 if key not found
        sets = qb.get((9, subject), qb.get((9, "Physics")))

    total_sets = len(sets)
    selected_set = sets[set_index % total_sets]

    return {
        "topic_title": selected_set["topic"],
        "questions": selected_set["questions"],
        "total_sets": total_sets
    }
