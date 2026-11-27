"""
EduAegis Comprehensive AI Tutor Curriculum Master Lessons
Provides rich, textbook-grade concept breakdowns for:
- Formal Board Standard Definitions
- Mathematical Formulas with Variable Definitions & SI Units
- Deep Conceptual Explanation (Physical/Mathematical Mechanisms & Derivations)
- Everyday Real-World Analogies
- Critical Board Exam Pitfalls & Misconceptions to Avoid
- How to Write Answers in Board Exams for Full Marks (Marking Rubrics)
- Audio Narration Script (Neutral Indian English Voice Modulation)
"""
from typing import Dict, Any

def get_comprehensive_tutor_lesson(active_topic: str, subject: str = "Physics", class_num: int = 9, board: str = "CBSE") -> Dict[str, Any]:
    """
    Returns an enriched, textbook-grade concept breakdown.
    """
    top_clean = (active_topic or "").strip().lower()

    # 1. NEWTON'S SECOND LAW & MOMENTUM (F = ma)
    if any(k in top_clean for k in ["newton's second", "newton 2nd", "second law", "momentum", "f = ma", "f=ma"]):
        return {
            "topic": "Newton's Second Law & Momentum (F = ma)",
            "subject": "Physics",
            "definition": (
                "Newton's Second Law of Motion states that the rate of change of momentum of a body "
                "is directly proportional to the applied unbalanced external force, and takes place "
                "in the direction in which the force acts."
            ),
            "formulas": [
                "Linear Momentum: p = m · v (SI Unit: kg·m/s or N·s)",
                "Rate of Change of Momentum: Δp / Δt = m(v - u) / t",
                "Newton's 2nd Law Equation: F = k · m · a ⟹ F = m · a (where k = 1 in SI units)",
                "SI Unit of Force: Newton (N), where 1 N = 1 kg·m/s²",
                "Impulse of a Force: J = F · Δt = Δp = m(v - u) (SI Unit: N·s)"
            ],
            "explanation": (
                "### 1. Conceptual Foundation: What is Momentum?\n"
                "In physics, **Linear Momentum ($p$)** represents the total 'quantity of motion' possessed by a moving object. "
                "It is mathematically defined as the product of an object's mass ($m$) and its velocity ($v$): $p = m \\cdot v$. "
                "Because velocity is a vector, momentum is also a vector having the exact same direction as velocity.\n\n"
                "- A massive freight train rolling slowly at 5 km/h possesses enormous momentum because of its colossal mass.\n"
                "- A tiny 10-gram bullet fired from a rifle at 800 m/s possesses massive momentum because of its extreme velocity.\n"
                "Both require an immense external force to bring to a halt!\n\n"
                "### 2. Derivation of $F = ma$ from First Principles (Board Standard)\n"
                "Consider an object of constant mass $m$ moving along a straight trajectory with an initial velocity $u$. "
                "Suppose an unbalanced external force $F$ acts on it continuously for a time duration of $t$ seconds, accelerating "
                "the object uniformly to a final velocity $v$.\n"
                "1. **Initial Momentum**: $p_1 = m \\cdot u$\n"
                "2. **Final Momentum**: $p_2 = m \\cdot v$\n"
                "3. **Change in Momentum**: $\\Delta p = p_2 - p_1 = m(v - u)$\n"
                "4. **Rate of Change of Momentum**: $\\frac{\\Delta p}{\\Delta t} = \\frac{m(v - u)}{t}$\n\n"
                "According to Newton's Second Law: $F \\propto \\frac{m(v - u)}{t}$.\n"
                "From kinematics, acceleration is $a = \\frac{v - u}{t}$. Substituting $a$ gives: $F \\propto m \\cdot a$.\n"
                "Introducing a proportionality constant $k$: $F = k \\cdot m \\cdot a$.\n"
                "In SI units, **1 Newton** is formally defined as the magnitude of force that produces an acceleration of $1\\text{ m/s}^2$ "
                "when applied to a mass of $1\\text{ kg}$. Setting $F = 1\\text{ N}, m = 1\\text{ kg}, a = 1\\text{ m/s}^2$ yields $k = 1$.\n"
                "Therefore, the fundamental equation of motion is **$F = m \\cdot a$**.\n\n"
                "### 3. The Impulse-Momentum Relationship ($F = \\frac{\\Delta p}{\\Delta t}$)\n"
                "Rearranging the law gives $F \\cdot \\Delta t = \\Delta p$. For a given fixed momentum change $\\Delta p$, "
                "the impact force $F$ is **inversely proportional** to the contact time $\\Delta t$ ($F \\propto \\frac{1}{\\Delta t}$). "
                "Prolonging the interaction time drastically reduces the peak destructive impact force experienced by colliding objects. "
                "This principle underpins automotive crash safety, sports bio-mechanics, and structural engineering."
            ),
            "analogies": [
                "Cricket Fielder Catching Technique: A fielder instinctively pulls his hands backward while gathering a high-velocity cricket ball. By increasing the stopping duration (Δt), the decelerating force on his palms is softened by over 70%, preventing severe hand bruising.",
                "High-Jump Foam Mat Cushioning: Athletes landing from heights land on thick, yielding foam mattresses or raked sand pits rather than solid concrete. The extra compression distance prolongs stopping time, keeping deceleration forces safely below bone-fracture thresholds.",
                "Automotive Airbags & Crumple Zones: During a collision, vehicle crumple zones deform progressively and airbags deploy in 30 milliseconds. This extends the passenger deceleration window, slashing the lethal peak forces acting on the chest and head."
            ],
            "pitfalls": [
                "Never confuse Mass (an invariant scalar in kg representing inertia) with Weight (a gravitational force vector in Newtons: W = mg).",
                "Do not merely write 'F = ma' as the verbal statement of the law. You MUST state: 'The rate of change of momentum is directly proportional to the applied unbalanced force...'",
                "Remember that force and acceleration are vectors pointing in the exact same direction; a forward-moving car experiencing brakes has an acceleration vector directed backward!"
            ],
            "board_tips": [
                "Step 1: Write the verbatim law: 'The rate of change of momentum of a body is directly proportional to the applied unbalanced force and occurs in the direction of the force.' (1 Mark)",
                "Step 2: Show the full algebraic derivation: p₁ = mu, p₂ = mv, Δp = m(v-u), Δp/t = ma, F = kma, k = 1 ⟹ F = ma. (2 Marks)",
                "Step 3: Define 1 Newton: '1 Newton is the force that imparts an acceleration of 1 m/s² to a mass of 1 kg.' (1 Mark)",
                "Step 4: Draw a cricket ball catch scenario and state F ∝ 1/Δt to secure the final application mark. (1 Mark)"
            ],
            "audio_text": (
                "Namaste and welcome students! Today let us master Newton's Second Law of Motion with textbook precision. "
                "Newton's Second Law states that the rate of change of momentum of a body is directly proportional to the applied "
                "unbalanced external force, and takes place in the direction of that force. "
                "Momentum is mass in motion, written as p equals m v. "
                "When a force acts over time t, the rate of change of momentum yields the fundamental equation: force equals mass "
                "times acceleration, F equals m a, measured in Newtons. "
                "Notice that for any fixed momentum change, force is inversely proportional to time. "
                "When a cricket fielder pulls his hands backward while catching a ball, he increases the stopping time, "
                "which drastically cushions the impact force on his palms. "
                "In your board exams, always state the formal law, show the step-by-step derivation, and define one Newton clearly to score full marks!"
            )
        }

    # 2. INERTIA AND FIRST LAW OF MOTION
    elif any(k in top_clean for k in ["inertia", "first law", "1st law"]):
        return {
            "topic": "Inertia and First Law of Motion",
            "subject": "Physics",
            "definition": (
                "Newton's First Law of Motion states that every body continues in its state of rest "
                "or of uniform motion in a straight line, unless it is compelled to change that state "
                "by an external unbalanced force. Inertia is the inherent property of an object by "
                "virtue of which it resists any change in its state of rest or uniform motion."
            ),
            "formulas": [
                "Equilibrium Condition: If ΣF_ext = 0, then a = 0 ⟹ v = constant (Zero Net Force)",
                "Quantitative Measure of Inertia: Inertia ∝ Mass (m in kg)",
                "Uniform Motion Equation: s = v · t (when acceleration a = 0)"
            ],
            "explanation": (
                "### 1. Galileo's Thought Experiment & The Principle of Inertia\n"
                "Prior to Galileo, ancient philosophers believed that a continuous sustaining force was required to keep objects in motion. "
                "Galileo disproved this misconception through his double inclined plane experiment: a smooth marble rolling down one ramp "
                "ascended an opposing ramp to virtually the exact same height regardless of ramp angle. Galileo deduced that if friction "
                "were completely eliminated, a body moving horizontally would continue coasting forever in a straight line at constant velocity.\n\n"
                "### 2. The Three Manifestations of Inertia\n"
                "Inertia expresses itself in three distinct physical forms:\n"
                "1. **Inertia of Rest**: The natural reluctance of a stationary object to initiate motion. When a stationary bus abruptly surges forward, standing passengers lurch backward. The floor accelerates their feet forward, but their torso stays at rest due to inertia.\n"
                "2. **Inertia of Motion**: The reluctance of a moving body to halt or decelerate. When a speeding bus hits the brakes suddenly, passengers pitch forward because their upper bodies preserve forward velocity while their feet are clamped by floor friction.\n"
                "3. **Inertia of Direction**: The reluctance of a body to alter its direction of travel. When an automobile takes a sharp turn around a curved road, passengers lean outward because their bodies tend to continue along the original straight line.\n\n"
                "### 3. Mass as the Quantitative Measure of Inertia\n"
                "Inertia is not a force; it is an intrinsic scalar property of matter. An empty cardboard box has small mass and minimal inertia, so a light kick moves it easily. A 50-kg solid iron boulder has large mass and massive inertia, requiring enormous force to alter its state."
            ),
            "analogies": [
                "Beating a Carpet with a Stick: Vigorously striking a hanging carpet forces the fabric forward; the trapped dust particles remain behind due to inertia of rest and drop to the floor under gravity.",
                "Shaking Fruit Trees: Vigorously shaking a mango or apple branch causes the branch to oscillate rapidly; the heavy fruits stay at rest due to inertia, snapping their stems.",
                "Long Jump Running Start: An athlete sprints before leaping into a long jump so that forward inertia of motion carries their body farther through the air."
            ],
            "pitfalls": [
                "Inertia is NOT a force. It is an intrinsic property directly proportional to mass.",
                "Do not confuse Newton's 1st Law with the 3rd Law (action-reaction acts on two different bodies, while inertia describes a single body's response to net force)."
            ],
            "board_tips": [
                "State the verbatim law mentioning both 'state of rest' and 'uniform motion in a straight line'.",
                "Explicitly identify Mass as the quantitative measure of inertia.",
                "Provide real-world examples for all three types: Inertia of Rest, Inertia of Motion, and Inertia of Direction."
            ],
            "audio_text": (
                "Welcome students! Today let us master Newton's First Law and Inertia. "
                "The First Law states that every object continues in its state of rest or uniform motion in a straight line "
                "unless compelled to change that state by an external unbalanced force. "
                "Inertia is the natural tendency of matter to resist any change in motion, and mass is its direct quantitative measure. "
                "Remember the three types: inertia of rest, seen when passengers lurch backward as a bus starts; "
                "inertia of motion, seen when passengers pitch forward upon sudden braking; "
                "and inertia of direction, seen when rounding a sharp curve. "
                "State these three types clearly with mass as the measure of inertia to score full marks in your exams!"
            )
        }

    # 3. UNIVERSAL GRAVITATION & FLOATATION
    elif any(k in top_clean for k in ["gravitat", "floatation", "buoyan", "archimedes"]):
        return {
            "topic": "Universal Gravitation & Floatation",
            "subject": "Physics",
            "definition": (
                "Newton's Universal Law of Gravitation states that every particle in the universe "
                "attracts every other particle with a force directly proportional to the product of "
                "their masses and inversely proportional to the square of the distance between their centers. "
                "Archimedes' Principle states that when a body is immersed wholly or partially in a fluid, "
                "it experiences an upward buoyant force equal to the weight of the fluid displaced by it."
            ),
            "formulas": [
                "Gravitational Force: F = G · (M₁ · M₂) / r²",
                "Universal Gravitational Constant: G = 6.674 × 10⁻¹¹ N·m²/kg²",
                "Acceleration due to Gravity: g = G·M / R² ≈ 9.8 m/s² (Earth's surface)",
                "Weight Equation: W = m · g (SI Unit: Newton, N)",
                "Buoyant Upthrust: F_B = V_displaced · ρ_fluid · g (Archimedes' Principle)",
                "Condition of Floatation: Floats if ρ_body ≤ ρ_fluid; Sinks if ρ_body > ρ_fluid"
            ],
            "explanation": (
                "### 1. The Universal Gravitational Interaction & Inverse Square Law\n"
                "Gravitation is a universal mutual attractive force operating between all entities possessing mass. "
                "The inverse square relationship ($F \\propto \\frac{1}{r^2}$) means that doubling the distance between two masses "
                "reduces gravitational pull to one-fourth ($1/4$), while tripling the separation reduces it to one-ninth ($1/9$).\n\n"
                "### 2. Crucial Distinction Between $G$ and $g$\n"
                "- **$G$ (Universal Gravitational Constant)**: $6.674 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2/\\text{kg}^2$. It is an absolute cosmic constant, identical everywhere on Earth, the Moon, or deep space.\n"
                "- **$g$ (Acceleration due to Gravity)**: Vector acceleration caused by gravity ($9.8\\text{ m/s}^2$ on Earth's surface, $1.63\\text{ m/s}^2$ on Moon). Because Earth is an oblate spheroid with a larger equatorial radius ($R_e > R_p$), $g$ is slightly higher at the poles ($9.83\\text{ m/s}^2$) than at the equator ($9.78\\text{ m/s}^2$).\n\n"
                "### 3. Buoyancy & Archimedes' Principle\n"
                "When an object is submerged in fluid, hydrostatic pressure increases with depth ($P = \\rho g h$). "
                "The pressure acting on the submerged bottom exceeds the pressure on the top, producing a net upward force called **Buoyant Force** or **Upthrust** ($F_B$). "
                "According to Archimedes' Principle, $F_B$ equals the weight of the displaced fluid. A solid steel needle sinks because its density ($7.8\\text{ g/cm}^3$) exceeds water ($1.0\\text{ g/cm}^3$). "
                "However, a giant steel ocean liner floats effortlessly because its vast hollow design displaces thousands of tons of water, generating buoyant upthrust equal to the ship's entire weight."
            ),
            "analogies": [
                "Oceanic Tides: High and low tides in Earth's oceans are caused by the gravitational pull of the Moon and Sun pulling on Earth's water bodies.",
                "Steel Needle vs Steel Cargo Ship: A 1-gram iron nail sinks immediately, but a 100,000-ton steel cruise ship floats because its hollow hull displaces huge water volume.",
                "Submarine Diving Mechanism: Submarines fill ballast tanks with seawater to increase total density to submerge, and pump compressed air into tanks to expel water when surfacing."
            ],
            "pitfalls": [
                "Never confuse capital G (Universal constant, N·m²/kg²) with lowercase g (local acceleration, m/s²).",
                "Astronauts in orbit are NOT in zero gravity! Gravity at 400 km is ~90% of surface gravity; weightlessness occurs because the spacecraft and astronauts are in continuous free-fall together."
            ],
            "board_tips": [
                "Construct a 4-row tabular comparison between G and g (Definition, Value & Units, Scalar/Vector, Constancy).",
                "State Archimedes' Principle verbatim and write apparent weight: W_apparent = W_actual - F_buoyant.",
                "Explain the condition of floatation using average density relative to fluid density."
            ],
            "audio_text": (
                "Hello students! Let us master Universal Gravitation and Floatation. "
                "Newton's Universal Law of Gravitation states that every mass in the universe attracts every other mass "
                "with a force directly proportional to the product of their masses and inversely proportional to the square of the distance between them. "
                "Capital G is the Universal Gravitational Constant, while lowercase g is the local acceleration due to gravity, roughly 9.8 meters per second squared on Earth. "
                "Meanwhile, Archimedes' Principle explains that an immersed object experiences an upward buoyant force equal to the weight of the fluid it displaces. "
                "A solid iron needle sinks because its density exceeds water, but a gigantic steel ship floats because its hollow shape displaces a vast volume of water, creating massive upward buoyancy. "
                "Remember these core definitions and formulas for full marks!"
            )
        }

    # 4. WORK, ENERGY & POWER
    elif any(k in top_clean for k in ["work", "energy", "power", "kinetic", "potential"]):
        return {
            "topic": "Work, Energy & Power",
            "subject": "Physics",
            "definition": (
                "Work is done on an object when an applied force produces a displacement in the direction of the force. "
                "Energy is the capacity to do work. Power is the rate of doing work or the rate of energy consumption."
            ),
            "formulas": [
                "Work Done: W = F · s · cos(θ) (SI Unit: Joule, J = N·m)",
                "Kinetic Energy: E_k = ½ · m · v² (SI Unit: Joule, J)",
                "Gravitational Potential Energy: E_p = m · g · h (SI Unit: Joule, J)",
                "Work-Energy Theorem: W_net = ΔE_k = ½mv² - ½mu²",
                "Power Equation: P = W / t = F · v (SI Unit: Watt, W = J/s; 1 HP = 746 W)",
                "Commercial Energy Unit: 1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ Joules"
            ],
            "explanation": (
                "### 1. Scientific Definition of Work ($W = F s \\cos\\theta$)\n"
                "In everyday language, mental effort is called 'work'. But in physics, work is strictly zero unless two conditions are met:\n"
                "1. A force must act on the object.\n"
                "2. The object must undergo non-zero displacement with a component along the direction of force.\n\n"
                "- **Positive Work ($\\theta = 0^\\circ$)**: Force and displacement are aligned (e.g. pulling a wagon forward).\n"
                "- **Zero Work ($\\theta = 90^\\circ$)**: Force is perpendicular to displacement. A railway coolie carrying a 40-kg trunk on his head across a flat platform does **zero work against gravity** because downward gravitational force acts at $90^\\circ$ to horizontal movement ($\\cos 90^\\circ = 0$).\n"
                "- **Negative Work ($\\theta = 180^\\circ$)**: Force opposes displacement (e.g. friction acting on a skidding car).\n\n"
                "### 2. Conservation of Mechanical Energy in Free Fall\n"
                "Consider an object of mass $m$ released from rest at height $H$:\n"
                "- At apex ($h = H$): $v = 0 \\implies E_k = 0, E_p = mgH \\implies E_{\\text{total}} = mgH$.\n"
                "- At midpoint ($h$): Velocity $v^2 = 2g(H - h) \\implies E_k = mg(H - h), E_p = mgh \\implies E_{\\text{total}} = mgH$.\n"
                "- At ground ($h = 0$): $v^2 = 2gH \\implies E_k = mgH, E_p = 0 \\implies E_{\\text{total}} = mgH$.\n"
                "Total mechanical energy ($E_k + E_p$) remains rigorously invariant throughout the fall!"
            ),
            "analogies": [
                "The Railway Coolie Paradox: Carrying heavy luggage horizontally results in zero work done against gravity because angle θ = 90° and cos 90° = 0.",
                "Hydroelectric Dam: Water held high behind a reservoir stores gravitational potential energy; falling down penstocks converts it into kinetic energy that spins generators.",
                "Roller Coaster Dynamics: A motor hoists the coaster to accumulate maximum potential energy at the peak, which smoothly trades into kinetic speed through descents."
            ],
            "pitfalls": [
                "Never confuse Power (rate of energy transfer, Watts = J/s) with Energy (total capacity to do work, Joules).",
                "Remember that home electric meters measure Energy in kilowatt-hours (kWh), not Power in kW!"
            ],
            "board_tips": [
                "State conditions for positive, zero, and negative work with theta angles (0°, 90°, 180°).",
                "Write the step-by-step free-fall energy conservation proof showing E = mgH at top, middle, and ground.",
                "Show calculation converting 1 kWh to 3.6 × 10⁶ Joules."
            ],
            "audio_text": (
                "Namaste students! Let us understand Work, Energy, and Power. "
                "Scientifically, work is done only when an applied force causes a displacement, calculated as force times displacement times cosine of theta. "
                "When you push against a rigid brick wall, displacement is zero, so no work is done. "
                "If a porter carries a heavy trunk horizontally, the force of gravity is perpendicular to motion, making work done against gravity zero. "
                "Energy is the capacity to do work, dividing into kinetic energy, half m v squared, and gravitational potential energy, m g h. "
                "In free fall, potential energy converts into kinetic energy while total mechanical energy remains strictly conserved. "
                "Power is the rate of doing work, measured in Watts. Keep these formulas and SI units sharp for your exams!"
            )
        }

    # 5. SOUND & WAVES
    elif any(k in top_clean for k in ["sound", "wave", "echo", "frequency", "ultrasound"]):
        return {
            "topic": "Sound & Waves",
            "subject": "Physics",
            "definition": (
                "Sound is a form of mechanical energy that propagates through an elastic material medium "
                "as a longitudinal wave of alternating compressions and rarefactions, initiated by vibrating bodies. "
                "Sound cannot propagate through a vacuum."
            ),
            "formulas": [
                "Wave Speed Equation: v = f · λ (Speed v in m/s, Frequency f in Hz, Wavelength λ in m)",
                "Time Period: T = 1 / f (seconds, s)",
                "Minimum Echo Distance: d_min = v · t / 2 = 344 × 0.1 / 2 = 17.2 meters (in air at 20°C)",
                "Loudness Proportionality: Loudness ∝ (Amplitude)²",
                "Speed Hierarchy in Media: v_solids > v_liquids > v_gases (v_steel ≈ 5960 m/s, v_air ≈ 344 m/s)"
            ],
            "explanation": (
                "### 1. Mechanical Propagation & Medium Requirement\n"
                "Unlike light (an electromagnetic transverse wave), sound is a mechanical longitudinal wave requiring a material medium with mass and elasticity. "
                "As a vibrating tuning fork prong flexes outward, it compresses nearby air particles into a high-pressure zone called a **Compression**. "
                "As it flexes inward, it creates a low-pressure zone called a **Rarefaction**.\n\n"
                "### 2. The Three Acoustic Characteristics of Sound\n"
                "1. **Pitch**: Governed by **Frequency ($f$)**. High frequency vibrations produce high-pitched, shrill tones (e.g. whistle, mosquito buzz); low frequency vibrations produce deep bass tones (e.g. bass drum, lion's roar).\n"
                "2. **Loudness**: Governed by **Amplitude ($A$)**. Loudness is proportional to amplitude squared ($L \\propto A^2$). Striking a tuning fork harder quadruples sound energy if amplitude is doubled.\n"
                "3. **Timbre / Quality**: Allows the human ear to distinguish two sounds having identical pitch and loudness (e.g. distinguishing a flute from a violin playing middle C due to harmonic waveforms).\n\n"
                "### 3. Echoes & Persistence of Hearing\n"
                "The human auditory cortex retains sensation of a sound for approximately **$0.1\\text{ seconds}$** (persistence of hearing). "
                "To hear a distinct echo, the reflected sound wave must return after at least $0.1\\text{ s}$. "
                "At $20^\\circ\\text{C}$ in air ($v = 344\\text{ m/s}$), total round-trip distance is $2d = v \\cdot t = 344 \\times 0.1 = 34.4\\text{ m}$, "
                "meaning the reflecting wall must be at least **$17.2\\text{ meters}$** away!"
            ),
            "analogies": [
                "Slinky Spring Oscillation: Pushing and pulling one end of a stretched slinky reproduces visible longitudinal compressions and rarefactions traveling down the coils.",
                "Thunder Following Lightning: Lightning flash and thunder happen simultaneously, but lightning is seen instantly (speed of light 300,000 km/s) while thunder rumbles seconds later (sound travels at only 0.34 km/s in air).",
                "Bat Echolocation & SONAR: Bats emit ultrasonic chirps (>20 kHz) to navigate and catch flying moths in complete darkness via echo reflection, exactly like ship SONAR systems."
            ],
            "pitfalls": [
                "Sound cannot travel in a vacuum! The bell-jar experiment proves that pumping out air silences a ringing electric bell.",
                "Never confuse Pitch (frequency) with Loudness (amplitude squared)."
            ],
            "board_tips": [
                "Draw a longitudinal wave graph showing Pressure/Density vs Distance with marked compressions and rarefactions.",
                "Derive minimum echo distance 17.2 m using persistence of hearing t = 0.1 s and 2d = vt.",
                "State human audible frequency spectrum: 20 Hz to 20,000 Hz (20 kHz)."
            ],
            "audio_text": (
                "Hello students! Let us explore Sound and Wave motion. "
                "Sound is a mechanical longitudinal wave produced by vibrating objects that travels through solids, liquids, "
                "and gases via alternating compressions and rarefactions. Sound cannot travel through a vacuum. "
                "The wave equation links wave speed to frequency and wavelength, written as v equals f times lambda. "
                "Frequency determines pitch, while amplitude determines loudness, where loudness is proportional to amplitude squared. "
                "To hear an echo clearly, the reflecting surface must be at least 17.2 meters away in air, due to our persistence of hearing of 0.1 seconds. "
                "Remember that sound travels fastest in solids and slowest in gases!"
            )
        }

    # 6. EVAPORATION & LATENT HEAT COOLING
    elif any(k in top_clean for k in ["evaporat", "latent heat", "cooling"]):
        return {
            "topic": "Evaporation & Latent Heat Cooling",
            "subject": "Chemistry",
            "definition": (
                "Evaporation is a spontaneous surface phenomenon in which a liquid transitions into vapor "
                "at any temperature below its boiling point. Latent Heat of Vaporization is the amount of heat energy "
                "absorbed by 1 kg of a liquid at its boiling point to change into vapor without any change in temperature."
            ),
            "formulas": [
                "Phase Change Heat: Q = m · L_v (SI Unit: Joule, J; for water L_v ≈ 2.26 × 10⁶ J/kg)",
                "Evaporation Proportionality: Rate ∝ Surface Area × Temperature × Wind Speed × (1 / Humidity)",
                "Latent Heat of Fusion: Q = m · L_f (for ice L_f ≈ 3.34 × 10⁵ J/kg)"
            ],
            "explanation": (
                "### 1. Molecular Mechanism of Evaporation\n"
                "In any liquid, molecules exist in perpetual thermal motion with a distribution of kinetic energies. "
                "A fraction of molecules located at the exposed surface possess kinetic energies sufficiently high to overcome "
                "the cohesive attractive intermolecular forces of neighboring liquid molecules. "
                "These energetic molecules break free from the liquid surface and enter the atmosphere as vapor.\n\n"
                "### 2. Why Evaporation Produces Cooling\n"
                "Because only the highest-energy molecules escape during evaporation, the average kinetic energy of the molecules "
                "remaining behind in the liquid decreases. Since temperature is directly proportional to average kinetic energy, "
                "the temperature of the remaining liquid drops. The liquid then absorbs heat (latent heat) from contacting surfaces, "
                "cooling the surrounding environment.\n\n"
                "### 3. The Four Determinants of Evaporation Rate\n"
                "1. **Surface Area**: Evaporation is strictly a surface phenomenon; larger surface area exposes more molecules to the air (e.g. spreading clothes wide to dry).\n"
                "2. **Temperature**: Higher temperature provides more kinetic energy to molecules, enabling more to escape.\n"
                "3. **Humidity**: Humidity measures ambient moisture content. If air is already humid, it holds little capacity for additional vapor, reducing evaporation.\n"
                "4. **Wind Speed**: Wind blows away vaporized molecules immediately above the surface, preventing local air saturation."
            ),
            "analogies": [
                "Indian Earthen Pitchers (Matkas): Thousands of microscopic pores in clay pots allow water to seep out; when this water evaporates, it absorbs latent heat from the pot and inner water, keeping water refreshingly cool in 45°C summers.",
                "Acetone / Hand Sanitizer on Palms: Highly volatile acetone evaporates rapidly from skin, absorbing latent heat directly from nerve endings to create an instant icy sensation.",
                "Cotton Clothing in Summer: Cotton fibers absorb sweat readily and wick it to the outer fabric surface, maximizing evaporative surface area to cool our bodies."
            ],
            "pitfalls": [
                "Never equate Evaporation (surface phenomenon at any temperature) with Boiling (bulk phenomenon at fixed boiling point with bubbles).",
                "Thermometer readings remain flat during latent heat absorption; heat energy is utilized to overcome intermolecular bonds, not raise temperature."
            ],
            "board_tips": [
                "Tabulate 4 differences between Evaporation and Boiling (Surface vs Bulk, Any temp vs Fixed temp, Silent vs Bubbling, Causes cooling vs No cooling).",
                "Explain the matka earthen pot cooling mechanism citing latent heat of vaporization.",
                "Detail why cotton garments are preferred in summer over polyester."
            ],
            "audio_text": (
                "Welcome students! Today let us master Evaporation and Latent Heat Cooling. "
                "Evaporation is a surface phenomenon where liquid particles at the surface absorb heat energy and escape as vapor "
                "at any temperature below the boiling point. "
                "When high-energy particles leave, the average kinetic energy of the remaining liquid drops, causing its temperature to decrease. "
                "The liquid then absorbs latent heat from its surroundings, producing a noticeable cooling effect. "
                "That is why water stays cool in porous earthen matkas, why acetone feels icy on your palm, and why cotton clothes keep us cool during Indian summers. "
                "In your exams, distinguish evaporation from boiling and highlight how surface area, temperature, wind speed, and humidity govern the rate of evaporation!"
            )
        }

    # 7. STATES OF MATTER & PHASE TRANSITIONS
    elif any(k in top_clean for k in ["states of matter", "phase transition", "sublimation", "solid", "liquid", "gas"]):
        return {
            "topic": "States of Matter & Phase Transitions",
            "subject": "Chemistry",
            "definition": (
                "Matter is anything that occupies space, has mass, and offers resistance. "
                "The three primary physical states—Solid, Liquid, and Gas—are determined by the competition "
                "between intermolecular forces of attraction and the kinetic energy of particles."
            ),
            "formulas": [
                "Temperature Conversion: K = °C + 273.15",
                "Density: ρ = m / V (SI Unit: kg/m³)",
                "Pressure: P = F / A (SI Unit: Pascal, Pa = N/m²; 1 atm = 1.013 × 10⁵ Pa)",
                "Phase Heat: Q = m · L (L_f for fusion, L_v for vaporization)"
            ],
            "explanation": (
                "### 1. Kinetic Molecular Characteristics of the Three States\n"
                "- **Solids**: Constituent particles are tightly bound in fixed crystalline or amorphous arrays with minimum intermolecular spaces and maximum intermolecular attraction. Solids possess definite shape and fixed volume with negligible compressibility.\n"
                "- **Liquids**: Particles have higher kinetic energy and can slide over one another. Intermolecular spaces are intermediate; liquids possess fixed volume but adopt the shape of their container, exhibiting fluidity.\n"
                "- **Gases**: Kinetic energy completely overwhelms intermolecular attraction. Particles move randomly at extreme speeds in all directions, with vast intermolecular gaps. Gases have neither fixed shape nor fixed volume, exhibiting high compressibility.\n\n"
                "### 2. Phase Transition Pathways\n"
                "- **Melting (Fusion)**: Solid $\\to$ Liquid (absorbs Latent Heat of Fusion).\n"
                "- **Boiling (Vaporization)**: Liquid $\\to$ Gas (absorbs Latent Heat of Vaporization).\n"
                "- **Sublimation**: Direct phase change from solid to gas without becoming a liquid (e.g. Camphor, Ammonium Chloride $\\text{NH}_4\\text{Cl}$, Naphthalene, and Dry Ice / solid $\\text{CO}_2$).\n"
                "- **Deposition**: Direct phase change from gas to solid.\n\n"
                "### 3. Latent Heat Plateau\n"
                "When heating a mixture of ice and water at $0^\\circ\\text{C}$, the temperature remains strictly stationary until all ice has completely melted. "
                "Supplied thermal energy does not increase particle kinetic velocity; it is consumed as latent heat to break crystalline hydrogen bonding."
            ),
            "analogies": [
                "Compressed Gas Cylinders (LPG & CNG): Tremendous gas compressibility allows hundreds of liters of fuel to be safely condensed into portable domestic metal cylinders.",
                "Sublimation of Naphthalene Balls: Mothballs placed in wool wardrobes gradually shrink and disappear over months without leaving any liquid residue.",
                "Steam Burns vs Boiling Water: Steam at 100°C causes significantly more severe tissue burns than boiling water at 100°C because every gram of steam delivers an extra 2260 Joules of latent heat."
            ],
            "pitfalls": [
                "Temperature does NOT rise during phase changes; energy is absorbed as latent heat.",
                "Never confuse Sublimation (solid to gas) with Evaporation (liquid to gas)."
            ],
            "board_tips": [
                "Draw the phase triangle diagram connecting Solid, Liquid, Gas with all 6 transition labels.",
                "Explain why steam burns are more severe than boiling water burns citing latent heat of vaporization.",
                "Name 3 sublimable compounds (Ammonium Chloride, Camphor, Solid CO₂)."
            ],
            "audio_text": (
                "Namaste students! Let us understand the States of Matter and Phase Transitions. "
                "Matter exists as solids, liquids, and gases based on particle kinetic energy and intermolecular attraction. "
                "Solids have fixed shape and volume; liquids flow with fixed volume; and gases compress easily to fill any container. "
                "When matter transitions between states, it absorbs or releases latent heat without changing temperature. "
                "For instance, melting ice absorbs latent heat of fusion at zero degrees Celsius. "
                "Sublimation occurs when a solid turns directly into a gas, seen in camphor and dry ice. "
                "Remember that steam at one hundred degrees causes worse burns than boiling water because steam contains extra latent heat of vaporization!"
            )
        }

    # 8. ATOMS, MOLECULES & CHEMICAL FORMULAS
    elif any(k in top_clean for k in ["atom", "molecule", "chemical formula", "valency", "mole concept"]):
        return {
            "topic": "Atoms, Molecules & Chemical Formulas",
            "subject": "Chemistry",
            "definition": (
                "An Atom is the smallest particle of an element that retains its chemical identity and takes part in chemical reactions. "
                "A Molecule is the smallest particle of an element or compound capable of independent existence. "
                "The Law of Conservation of Mass states that mass can neither be created nor destroyed in a chemical reaction. "
                "The Law of Constant Proportions states that a pure chemical compound always contains elements in fixed proportions by mass."
            ),
            "formulas": [
                "Avogadro's Number: 1 mole = 6.022 × 10²³ particles (N_A)",
                "Number of Moles: n = Given Mass (m) / Molar Mass (M) = Particles (N) / N_A",
                "Molecular Mass: Sum of atomic masses in unified atomic mass units (u or g/mol)",
                "Criss-Cross Valency Rule: Cation^x+ + Anion^y- ⟹ A_y B_x"
            ],
            "explanation": (
                "### 1. The Two Bedrock Laws of Chemical Combination\n"
                "1. **Law of Conservation of Mass (Lavoisier)**: In any closed chemical reaction, the total mass of the reactants identically equals the total mass of the products.\n"
                "2. **Law of Constant Proportions (Proust)**: In a chemical substance, the elements are always present in definite proportions by mass. For instance, in water ($\\text{H}_2\\text{O}$), the ratio of the mass of hydrogen to oxygen is always $1:8$, whether collected from rain, tap, or river.\n\n"
                "### 2. The Criss-Cross Valency Rule for Writing Formulas\n"
                "To write the formula of an ionic or covalent compound:\n"
                "1. Write the symbols of the elements or polyatomic ions side by side (cation on left, anion on right).\n"
                "2. Write their valencies underneath each symbol.\n"
                "3. Criss-cross the valencies to become subscripts for the opposite partner.\n"
                "4. Enclose polyatomic ions in parentheses if subscript is $> 1$.\n\n"
                "*Examples*:\n"
                "- Calcium Hydroxide: $\\text{Ca}^{2+}$ and $\\text{OH}^- \\implies \\text{Ca}_1(\\text{OH})_2 \\implies \\mathbf{\\text{Ca(OH)}_2}$\n"
                "- Aluminium Oxide: $\\text{Al}^{3+}$ and $\\text{O}^{2-} \\implies \\mathbf{\\text{Al}_2\\text{O}_3}$\n"
                "- Sodium Carbonate: $\\text{Na}^+$ and $\\text{CO}_3^{2-} \\implies \\mathbf{\\text{Na}_2\\text{CO}_3}$\n\n"
                "### 3. The Mole Concept as a Counting Bridge\n"
                "One mole contains exactly $6.022 \\times 10^{23}$ elementary entities. It connects macroscopic laboratory gram weights with microscopic numbers of atoms: 1 mole of carbon atoms weighs $12\\text{ grams}$ and contains $6.022 \\times 10^{23}$ carbon atoms."
            ),
            "analogies": [
                "Dozen vs Mole: Just as 1 dozen always represents 12 items (whether eggs or apples), 1 mole always represents 6.022 × 10²³ particles (whether atoms or molecules).",
                "Baking Cake Recipe: In baking, ingredients must follow exact ratios; in water, 2 grams of hydrogen always combine with 16 grams of oxygen (1:8 by mass)."
            ],
            "pitfalls": [
                "Forgetting parentheses for polyatomic ions (writing CaOH₂ instead of Ca(OH)₂ loses full marks).",
                "Confusing molecular mass (in unified atomic mass units 'u') with molar mass (in 'g/mol')."
            ],
            "board_tips": [
                "State the two laws of chemical combination with illustrative numerical mass ratios.",
                "Show the criss-cross valency working table step-by-step for polyatomic compounds.",
                "Memorize standard atomic masses: H=1, C=12, N=14, O=16, Na=23, Mg=24, Al=27, S=32, Cl=35.5, Ca=40."
            ],
            "audio_text": (
                "Hello students! Let us master Atoms, Molecules, and Chemical Formulas. "
                "Chemistry is built on two foundational laws: the Law of Conservation of Mass, which states mass cannot be created or destroyed, "
                "and the Law of Constant Proportions, stating elements combine in fixed ratios by mass. "
                "To write chemical formulas, we use the criss-cross valency method. "
                "For calcium hydroxide, calcium has valency plus two and hydroxide has minus one, criss-crossing to form Ca OH twice, with OH in brackets. "
                "The mole concept bridges the atomic world to the laboratory scale, where one mole equals six point zero two two times ten to the twenty-third particles. "
                "Master these formula rules and mole conversions for top board exam scores!"
            )
        }

    # 9. STRUCTURE OF THE ATOM
    elif any(k in top_clean for k in ["structure of the atom", "rutherford", "bohr", "electron", "proton", "neutron", "isotope", "isobar"]):
        return {
            "topic": "Structure of the Atom",
            "subject": "Chemistry",
            "definition": (
                "An atom consists of three subatomic particles: positively charged protons and neutral neutrons "
                "concentrated in a dense, central nucleus, surrounded by negatively charged electrons "
                "revolving in discrete, quantized energy orbits called shells."
            ),
            "formulas": [
                "Atomic Number: Z = Number of Protons = Number of Electrons (neutral atom)",
                "Mass Number: A = Protons (Z) + Neutrons (n) ⟹ A = Z + n",
                "Bohr-Bury Maximum Shell Capacity: 2n² (K=2, L=8, M=18, N=32)",
                "Octet Valence Rule: Max valence electrons in outermost shell ≤ 8",
                "Nuclide Symbol: ᴬ_Z X (e.g. ²³_11 Na, ³⁵_17 Cl)"
            ],
            "explanation": (
                "### 1. Rutherford's Gold Foil $\\alpha$-Scattering Experiment\n"
                "Rutherford bombarded an ultra-thin sheet of gold foil with fast-moving alpha particles ($^4_2\\text{He}^{2+}$):\n"
                "1. **Most $\\alpha$-particles passed undeflected** $\\implies$ Most of the space inside an atom is empty.\n"
                "2. **A few particles deflected by small and large angles** $\\implies$ Positive charge is concentrated in a tiny volume.\n"
                "3. **1 in 12,000 rebounded by $180^\\circ$** $\\implies$ Nearly all mass and positive charge is packed into an ultra-dense central core named the **Nucleus**.\n\n"
                "### 2. Bohr's Model of the Atom\n"
                "To resolve why orbiting electrons do not radiate energy and spiral into the nucleus, Neils Bohr postulated:\n"
                "- Electrons revolve only in discrete, non-radiating orbits known as **stationary energy levels** ($K, L, M, N$ or $n=1, 2, 3, 4$).\n"
                "- Electrons emit or absorb energy only when jumping between energy levels: $\\Delta E = E_2 - E_1 = h \\nu$.\n\n"
                "### 3. Isotopes and Isobars\n"
                "- **Isotopes**: Atoms of the same element having identical atomic number ($Z$) but differing mass numbers ($A$). E.g. $^{35}_{17}\\text{Cl}$ and $^{37}_{17}\\text{Cl}$; Protium $^1_1\\text{H}$, Deuterium $^2_1\\text{H}$, Tritium $^3_1\\text{H}$. They share identical chemical properties due to matching valence electrons.\n"
                "- **Isobars**: Atoms of different elements having different atomic numbers ($Z$) but identical mass number ($A$). E.g. Argon $^{40}_{18}\\text{Ar}$ and Calcium $^{40}_{20}\\text{Ca}$."
            ),
            "analogies": [
                "Stadium and Cricket Ball: If an atom were enlarged to the size of a giant cricket stadium, the nucleus at the center would be the size of a small pea on the pitch, showing that an atom is over 99.999% empty space.",
                "Planetary Orbits: Electrons orbit the central nucleus much like planets orbit the sun, but strictly confined to quantized energy tracks."
            ],
            "pitfalls": [
                "Do not confuse Isotopes (same Z, different A) with Isobars (different Z, same A).",
                "Remember mass number A is always an integer (number of nucleons), while fractional atomic masses arise from isotopic abundance averages."
            ],
            "board_tips": [
                "State Rutherford's 3 observations alongside their exact 3 deductions.",
                "Draw Bohr's model for elements 1 to 20 showing electron configurations using 2n² and octet rules.",
                "Define Isotopes and Isobars with two standard examples for each."
            ],
            "audio_text": (
                "Namaste students! Let us understand the Structure of the Atom. "
                "An atom contains a dense central nucleus with protons and neutrons, orbited by electrons in discrete energy shells. "
                "Rutherford's gold foil experiment proved that atoms are mostly empty space, with virtually all mass packed into a positive nucleus. "
                "Neils Bohr explained that electrons travel in stable, non-radiating energy shells labeled K, L, M, N, with maximum capacities given by two n squared. "
                "Isotopes are atoms of the same element with identical atomic numbers but different mass numbers, like chlorine thirty-five and thirty-seven. "
                "Isobars are atoms of different elements with the same mass number, like argon forty and calcium forty. "
                "Remember these shell capacities and subatomic properties for top exam marks!"
            )
        }

    # 10. RATIONAL VS IRRATIONAL NUMBERS
    elif any(k in top_clean for k in ["rational vs", "irrational", "real number"]):
        return {
            "topic": "Rational vs Irrational Numbers",
            "subject": "Mathematics",
            "definition": (
                "A Rational Number is any number that can be expressed in the form p/q, where p and q are integers and q ≠ 0. "
                "An Irrational Number cannot be expressed in the form p/q; its decimal expansion is non-terminating and non-recurring."
            ),
            "formulas": [
                "Rational Form: p / q (p, q ∈ ℤ, q ≠ 0)",
                "Terminating Decimal Rule: Prime factors of q = 2ᵐ · 5ⁿ (where m, n ≥ 0)",
                "Irrational Decimals: Non-terminating and non-recurring (e.g. √2, √3, √5, π)",
                "Real Numbers Set: ℝ = ℚ ∪ ℚ' (Union of Rational and Irrational numbers)",
                "Operations: Rational + Irrational = Irrational; Non-zero Rational × Irrational = Irrational"
            ],
            "explanation": (
                "### 1. Decimal Classification of Real Numbers\n"
                "Every real number has a unique decimal representation:\n"
                "1. **Terminating Decimals**: The division terminates with remainder zero (e.g. $\\frac{3}{8} = 0.375$). The denominator in simplest form contains prime factors of 2 and/or 5 exclusively.\n"
                "2. **Non-Terminating Repeating Decimals**: Digits repeat infinitely in a recurring block (e.g. $\\frac{1}{3} = 0.\\overline{3}$, $\\frac{2}{7} = 0.\\overline{285714}$). These are **Rational** numbers.\n"
                "3. **Non-Terminating Non-Repeating Decimals**: Digits continue endlessly without any repeating pattern (e.g. $\\sqrt{2} = 1.41421356...$). These are **Irrational** numbers.\n\n"
                "### 2. Proof of Irrationality of $\\sqrt{2}$ by Contradiction\n"
                "1. Assume $\\sqrt{2}$ is rational: $\\sqrt{2} = \\frac{a}{b}$, where $a, b$ are coprime integers ($b \\neq 0$).\n"
                "2. Squaring both sides: $2 = \\frac{a^2}{b^2} \\implies 2b^2 = a^2$.\n"
                "3. This means $a^2$ is divisible by 2, which implies $a$ is divisible by 2. Let $a = 2c$.\n"
                "4. Substituting: $2b^2 = (2c)^2 = 4c^2 \\implies b^2 = 2c^2$.\n"
                "5. This implies $b^2$ is divisible by 2, so $b$ is also divisible by 2.\n"
                "6. Thus, 2 is a common factor of both $a$ and $b$, contradicting the premise that $a$ and $b$ are coprime. Hence, $\\sqrt{2}$ is irrational!"
            ),
            "analogies": [
                "Clockwork vs Free Explorer: Rational numbers repeat predictably like clockwork hands (0.333...); irrational decimals explore uncharted territory endlessly without repeating.",
                "Pi (π) vs 22/7: In board exams, students often confuse π with 22/7. 22/7 is a rational approximation (3.142857...), whereas true π is an irrational number."
            ],
            "pitfalls": [
                "Never claim π is rational because it equals 22/7; 22/7 is merely an approximation.",
                "The sum of two irrationals is not always irrational: (3 + √2) + (3 - √2) = 6 (rational)!"
            ],
            "board_tips": [
                "Memorize the 6-step proof by contradiction for √2 and √5 specifying 'coprime integers'.",
                "Show algebraic conversion of recurring decimals 0.6̄ to p/q using 10x - x = 9x."
            ],
            "audio_text": (
                "Welcome students! Today we master Rational and Irrational Numbers. "
                "A rational number can always be written as a fraction p over q, where p and q are integers and q is non-zero. "
                "Its decimal expansion either terminates or repeats predictably. "
                "If the denominator's prime factorization contains only twos and fives, the decimal terminates. "
                "In contrast, an irrational number like square root of two or pi has a decimal that continues forever without repeating. "
                "Remember that proving square root of two is irrational by contradiction is a classic board exam question. "
                "Follow the step-by-step coprime proof to score full marks!"
            )
        }

    # 11. RATIONALIZING THE DENOMINATOR
    elif any(k in top_clean for k in ["rationaliz", "denominator", "conjugate"]):
        return {
            "topic": "Rationalizing the Denominator",
            "subject": "Mathematics",
            "definition": (
                "Rationalizing the denominator is the algebraic process of converting a fraction with an irrational "
                "radical in the denominator into an equivalent fraction with a rational denominator, "
                "by multiplying both numerator and denominator by a suitable conjugate."
            ),
            "formulas": [
                "Monomial Surd Rule: 1 / √a = 1/√a × √a/√a = √a / a",
                "Binomial Conjugate Pair: (a + √b)(a - √b) = a² - b",
                "Radical Conjugate Pair: (√a + √b)(√a - √b) = a - b",
                "Standard Form: k / (a + √b) = k(a - √b) / (a² - b)"
            ],
            "explanation": (
                "### 1. Why Do We Rationalize?\n"
                "Dividing a number by an endless non-repeating decimal (such as dividing $1$ by $\\sqrt{2} \\approx 1.41421...$) is computationally difficult. "
                "By rationalizing the denominator, we convert the divisor into a clean integer: $\\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2} \\approx \\frac{1.41421}{2} = 0.7071$.\n\n"
                "### 2. Worked Textbook Solutions Step-by-Step\n"
                "**Problem 1**: Rationalize the denominator of $\\frac{1}{7 + 3\\sqrt{2}}$.\n"
                "1. Identify the conjugate of $(7 + 3\\sqrt{2})$, which is $(7 - 3\\sqrt{2})$.\n"
                "2. Multiply numerator and denominator by $(7 - 3\\sqrt{2})$:\n"
                "   $$\\frac{1}{7 + 3\\sqrt{2}} \\times \\frac{7 - 3\\sqrt{2}}{7 - 3\\sqrt{2}}$$\n"
                "3. Apply algebraic identity $(x + y)(x - y) = x^2 - y^2$ to the denominator:\n"
                "   $$\\text{Denominator} = 7^2 - (3\\sqrt{2})^2 = 49 - (9 \\times 2) = 49 - 18 = 31$$\n"
                "4. Final Simplified Result:\n"
                "   $$\\frac{7 - 3\\sqrt{2}}{31}$$\n\n"
                "**Problem 2**: Rationalize $\\frac{\\sqrt{3} - \\sqrt{2}}{\\sqrt{3} + \\sqrt{2}}$.\n"
                "Multiply by conjugate $(\\sqrt{3} - \\sqrt{2})$:\n"
                "$$\\frac{(\\sqrt{3} - \\sqrt{2})^2}{(\\sqrt{3})^2 - (\\sqrt{2})^2} = \\frac{3 - 2\\sqrt{6} + 2}{3 - 2} = 5 - 2\\sqrt{6}$$"
            ),
            "analogies": [
                "Clean Division: Rationalizing flips an awkward division so that tricky roots sit on top as multipliers while the divisor below is a simple whole integer."
            ],
            "pitfalls": [
                "Squaring (3√2)² incorrectly: remember (3√2)² = 3² × (√2)² = 9 × 2 = 18.",
                "Forgetting to multiply the numerator by the conjugate, which alters the value of the fraction."
            ],
            "board_tips": [
                "State the algebraic identity used: (a + b)(a - b) = a² - b².",
                "Show distinct steps for numerator expansion and denominator subtraction."
            ],
            "audio_text": (
                "Hello students! Let us master Rationalizing the Denominator. "
                "When a fraction has a square root in the denominator, dividing by an endless decimal is difficult. "
                "We rationalize by multiplying both the top and bottom by the conjugate of the denominator, utilizing the algebraic identity a plus b times a minus b equals a squared minus b squared. "
                "For example, to rationalize one over seven plus three root two, multiply numerator and denominator by seven minus three root two. "
                "The denominator becomes seven squared minus three root two squared, which is forty-nine minus eighteen, giving thirty-one. "
                "The final answer is seven minus three root two, all divided by thirty-one. "
                "Always show each calculation step in your board exams for full marks!"
            )
        }

    # 12. LAWS OF EXPONENTS
    elif any(k in top_clean for k in ["exponent", "power", "indices", "law of exponent"]):
        return {
            "topic": "Laws of Exponents",
            "subject": "Mathematics",
            "definition": (
                "The Laws of Exponents provide fundamental algebraic rules that govern the simplification, "
                "multiplication, division, and exponentiation of powers with identical or different bases."
            ),
            "formulas": [
                "Product Rule: aᵐ · aⁿ = aᵐ⁺ⁿ",
                "Quotient Rule: aᵐ / aⁿ = aᵐ⁻ⁿ (for a ≠ 0)",
                "Power of a Power: (aᵐ)ⁿ = aᵐ·ⁿ",
                "Power of a Product: (a · b)ⁿ = aⁿ · bⁿ",
                "Power of a Quotient: (a / b)ⁿ = aⁿ / bⁿ (for b ≠ 0)",
                "Zero Exponent Identity: a⁰ = 1 (for any real a ≠ 0)",
                "Negative Exponent Rule: a⁻ⁿ = 1 / aⁿ",
                "Fractional Exponent Rule: aᵐ/ⁿ = ⁿ√(aᵐ) = (ⁿ√a)ᵐ"
            ],
            "explanation": (
                "### 1. Conceptual Foundation of Powers\n"
                "An exponent indicates repeated multiplication ($a^3 = a \\times a \\times a$). "
                "When multiplying powers with matching bases, exponents add because total factors accumulate: $a^2 \\cdot a^3 = (a \\cdot a)(a \\cdot a \\cdot a) = a^5$.\n\n"
                "### 2. Why Does $a^0 = 1$?\n"
                "Using the quotient law: $\\frac{a^m}{a^m} = a^{m - m} = a^0$. "
                "However, any non-zero number divided by itself identically equals 1. Therefore, $a^0 = 1$ by mathematical definition!\n\n"
                "### 3. Evaluating Rational Exponents Step-by-Step\n"
                "**Example 1**: Evaluate $(64)^{2/3}$.\n"
                "- Write base as a prime power: $64 = 4^3$ (or $2^6$).\n"
                "- Apply power of a power rule: $(4^3)^{2/3} = 4^{3 \\times (2/3)} = 4^2 = 16$.\n\n"
                "**Example 2**: Evaluate $(125)^{-1/3}$.\n"
                "- Express 125 as $5^3$: $(5^3)^{-1/3} = 5^{3 \\times (-1/3)} = 5^{-1} = \\frac{1}{5}$."
            ),
            "analogies": [
                "Folding Paper Doubling: Folding a paper sheet in half 10 times produces 2¹⁰ = 1024 layers, demonstrating the explosive power of exponents."
            ],
            "pitfalls": [
                "Do not confuse aᵐ · aⁿ = aᵐ⁺ⁿ with (aᵐ)ⁿ = aᵐⁿ.",
                "Notice that (-2)⁴ = +16, but -2⁴ = -16 (brackets matter!)."
            ],
            "board_tips": [
                "Always decompose composite bases (64, 125, 243) into prime bases before applying laws of exponents.",
                "Quote each exponent law in brackets next to each step."
            ],
            "audio_text": (
                "Welcome students! Today let us master the Laws of Exponents. "
                "When multiplying powers with the same base, add their exponents: a to the m times a to the n equals a to the m plus n. "
                "When dividing, subtract exponents. A power raised to another power multiplies exponents: a to the m raised to n equals a to the m times n. "
                "Any non-zero number to the power of zero is one, because a to the m divided by a to the m equals one. "
                "For fractional exponents like sixty-four to the two-thirds, write sixty-four as four cubed. "
                "Four cubed raised to two-thirds gives four squared, which equals sixteen. "
                "Always factor numbers into prime bases to solve exponent questions easily in exams!"
            )
        }

    # 13. POLYNOMIALS & FACTORIZATION
    elif any(k in top_clean for k in ["polynomial", "factoriz", "remainder theorem", "factor theorem", "middle term"]):
        return {
            "topic": "Polynomials & Factorization",
            "subject": "Mathematics",
            "definition": (
                "A Polynomial P(x) in one variable x is an algebraic expression of the form "
                "aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀, where exponents of x are non-negative integers. "
                "Factorization is the process of expressing a polynomial as a product of simpler irreducible factors."
            ),
            "formulas": [
                "Remainder Theorem: When P(x) is divided by (x - a), the remainder is R = P(a)",
                "Factor Theorem: (x - a) is a factor of P(x) if and only if P(a) = 0",
                "Quadratic Expansion: (a + b)² = a² + 2ab + b²",
                "Difference of Squares: a² - b² = (a - b)(a + b)",
                "Cubic Identity: (a + b)³ = a³ + b³ + 3ab(a + b)",
                "Three-Term Cubic Identity: a³ + b³ + c³ - 3abc = (a + b + c)(a² + b² + c² - ab - bc - ca)",
                "Conditional Identity: If a + b + c = 0, then a³ + b³ + c³ = 3abc"
            ],
            "explanation": (
                "### 1. Polynomial Classification & Validity\n"
                "An algebraic expression is a valid polynomial only if all powers of $x$ are whole numbers ($0, 1, 2...$). "
                "Expressions with fractional exponents (like $\\sqrt{x} = x^{1/2}$) or negative exponents (like $\\frac{1}{x} = x^{-1}$) are **NOT** polynomials.\n\n"
                "### 2. Splitting the Middle Term Method for Quadratics ($ax^2 + bx + c$)\n"
                "To factorize $6x^2 + 17x + 5$:\n"
                "1. Find two numbers $p$ and $q$ such that $p + q = 17$ (the middle coefficient) and $p \\times q = a \\times c = 6 \\times 5 = 30$.\n"
                "2. The numbers are $15$ and $2$ ($15 + 2 = 17$, $15 \\times 2 = 30$).\n"
                "3. Split the middle term: $6x^2 + 15x + 2x + 5$.\n"
                "4. Factor by grouping: $3x(2x + 5) + 1(2x + 5) = (2x + 5)(3x + 1)$.\n\n"
                "### 3. Factorizing Cubics via Factor Theorem\n"
                "To factorize $P(x) = x^3 - 23x^2 + 142x - 120$:\n"
                "1. Test factors of constant term ($\\pm 1, \\pm 2...$). Since $P(1) = 1 - 23 + 142 - 120 = 0$, by the Factor Theorem $(x - 1)$ is a factor.\n"
                "2. Divide $P(x)$ by $(x - 1)$ to get quadratic $(x^2 - 22x + 120)$.\n"
                "3. Factorize quadratic into $(x - 10)(x - 12)$. Total factors: $(x - 1)(x - 10)(x - 12)$."
            ),
            "analogies": [
                "Decomposing Molecules: Factorization is like breaking a complex chemical compound into its fundamental constituent atoms."
            ],
            "pitfalls": [
                "Powers must be whole numbers; √x or 1/x cannot be part of a polynomial.",
                "Be vigilant with signs when expanding (a - b)³ = a³ - b³ - 3ab(a - b)."
            ],
            "board_tips": [
                "Use conditional identity if a + b + c = 0 for cubic evaluations without direct computation.",
                "Show remainder clearly using Remainder Theorem R = P(a)."
            ],
            "audio_text": (
                "Namaste students! Let us master Polynomials and Factorization. "
                "A polynomial is an algebraic expression with non-negative integer exponents. "
                "The Remainder Theorem states that dividing P of x by x minus a leaves a remainder of P of a. "
                "If P of a equals zero, the Factor Theorem guarantees that x minus a is an exact factor. "
                "To factorize quadratics like six x squared plus seventeen x plus five, split the middle term into fifteen x and two x, giving two x plus five times three x plus one. "
                "For cubics, find the first root by trial, then divide to get the quadratic factor. "
                "Also remember: if a plus b plus c equals zero, then a cubed plus b cubed plus c cubed equals three a b c. "
                "Master these identities for full marks!"
            )
        }

    # 14. LINEAR EQUATIONS
    elif any(k in top_clean for k in ["linear equation", "two variables", "straight line", "cartesian"]):
        return {
            "topic": "Linear Equations in Two Variables",
            "subject": "Mathematics",
            "definition": (
                "A Linear Equation in two variables is an algebraic equation of the form ax + by + c = 0, "
                "where a, b, c are real numbers and a and b are not both zero. "
                "Its geometrical representation on the Cartesian plane is always a straight line."
            ),
            "formulas": [
                "Standard Form: ax + by + c = 0 (a, b not both 0)",
                "Slope-Intercept Form: y = m · x + c (where slope m = -a/b, intercept = -c/b)",
                "Vertical Line (parallel to y-axis): x = k (slope undefined)",
                "Horizontal Line (parallel to x-axis): y = k (slope = 0)",
                "Equation of X-axis: y = 0; Equation of Y-axis: x = 0",
                "Infinitely Many Solutions: Every coordinate point (x, y) on the line is a valid solution"
            ],
            "explanation": (
                "### 1. Infinitely Many Solutions Principle\n"
                "A linear equation in two variables has an infinite number of solutions. "
                "Every ordered pair $(x_1, y_1)$ that satisfies $a x_1 + b y_1 + c = 0$ corresponds to a unique point on the line, "
                "and every point lying on the line satisfies the equation.\n\n"
                "### 2. Plotting a Linear Equation Step-by-Step\n"
                "To plot $2x + 3y = 12$ on a Cartesian coordinate plane:\n"
                "1. Express $y$ explicitly in terms of $x$: $y = \\frac{12 - 2x}{3}$.\n"
                "2. Compute three coordinate pairs:\n"
                "   - Let $x = 0 \\implies y = 4 \\implies (0, 4)$ [Y-intercept]\n"
                "   - Let $y = 0 \\implies 2x = 12 \\implies x = 6 \\implies (6, 0)$ [X-intercept]\n"
                "   - Let $x = 3 \\implies y = \\frac{12 - 6}{3} = 2 \\implies (3, 2)$\n"
                "3. Plot $(0, 4)$, $(6, 0)$, and $(3, 2)$ on graph axes and draw a continuous straight ruler line through them."
            ),
            "analogies": [
                "GPS Highway Trajectory: A straight national highway is governed by a linear equation; every kilometer milestone (x, y) along the route satisfies that exact relationship."
            ],
            "pitfalls": [
                "Do not confuse the equation of the x-axis (y = 0) with the y-axis (x = 0).",
                "A single linear equation in two variables has infinitely many solutions, not a unique solution."
            ],
            "board_tips": [
                "Always plot at least 3 points to confirm collinearity; 2 points can mask arithmetic errors.",
                "Label the x and y axes, origin (0,0), and scale clearly."
            ],
            "audio_text": (
                "Welcome students! Today let us master Linear Equations in two variables. "
                "An equation of the form a x plus b y plus c equals zero represents a straight line on the Cartesian plane and has infinitely many solutions. "
                "Every solution pair corresponds to a point lying on that straight line. "
                "The equation of the x-axis is y equals zero, while the equation of the y-axis is x equals zero. "
                "To draw the graph, find at least three coordinate points, such as the x and y intercepts, plot them, and draw a straight line through them with a ruler. "
                "Master these plotting methods and slope equations for full marks in your board exams!"
            )
        }

    # DYNAMIC FALLBACK / CUSTOM TOPIC / INGESTED CONTENT
    else:
        topic_title = active_topic.strip() if active_topic and active_topic.strip() else f"Fundamental Concepts in {subject}"
        return {
            "topic": topic_title,
            "subject": subject,
            "definition": (
                f"{topic_title} is a fundamental concept in {board} Class {class_num}th {subject}, "
                f"governed by precise scientific and mathematical laws, empirical observations, and logical principles."
            ),
            "formulas": [
                f"Governing Principle: Standard {subject} Formulation",
                f"Quantitative Relation: Expressed in SI Metric Units for Class {class_num}th {board} Curriculum",
                f"Conservation Law: Conserved in Isolated Ideal Systems"
            ],
            "explanation": (
                f"### 1. Core Theoretical Mechanism of {topic_title}\n"
                f"In {subject}, every observable phenomenon is governed by an underlying cause-and-effect physical mechanism. "
                f"Understanding **{topic_title}** requires identifying the independent variables, dependent responses, and governing boundary conditions.\n\n"
                f"### 2. Analytical Breakdown & Derivation\n"
                f"When analyzing {topic_title} for {board} examinations, structure your conceptual reasoning through three foundational stages:\n"
                f"1. **Stating Assumptions**: Clarify the frame of reference, mass invariance, and operating constraints.\n"
                f"2. **Mathematical Formulation**: Set up the governing algebraic equations with explicit variable definitions.\n"
                f"3. **Physical Interpretation**: Verify dimensions and units on both sides of the equation to ensure dimensional consistency.\n\n"
                f"### 3. Real-World Applications & Scientific Impact\n"
                f"This principle is widely deployed in industrial engineering, everyday household technologies, and modern scientific research."
            ),
            "analogies": [
                f"Relating {topic_title} to everyday observable physical and biological systems in our daily environment.",
                f"Observing cause-and-effect relationships under changing experimental variables."
            ],
            "pitfalls": [
                f"Avoid writing vague answers; always quote the exact scientific term and SI units.",
                f"Never skip stating the boundary conditions or assumptions under which the law holds true."
            ],
            "board_tips": [
                f"Step 1: Write a crisp formal definition with standard keywords. (1 Mark)",
                f"Step 2: State the mathematical formula with variable definitions and metric SI units. (2 Marks)",
                f"Step 3: Provide a neat labeled diagram or a real-world application. (1 Mark)"
            ],
            "audio_text": (
                f"Namaste students! Let us understand {topic_title} with absolute conceptual clarity. "
                f"In {subject}, every concept is governed by cause and effect. "
                f"For your {board} Class {class_num}th examinations, always structure your answers with three clear pillars: "
                f"First, a crisp definition. Second, the exact mathematical formula with SI units. "
                f"And third, an everyday real-world example. Clear step-by-step presentation guarantees full marks!"
            )
        }
