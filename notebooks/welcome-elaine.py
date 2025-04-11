

import marimo

__generated_with = "0.12.8"
app = marimo.App(
    width="medium",
    layout_file="layouts/welcome-elaine.slides.json",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# Seja bem-vinda, Elaine!""")
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    # Create an accordion component with the personal message inside

    def create_accordion_message():
        # Create the accordion component
        accordion = mo.accordion(
            {
                "A Letter for Elaine ": f"""
                <div style="background-color: #fff8e1; border-radius: 8px; padding: 20px; border: 1px solid #ffecb3; 
                      font-family: 'Garamond', monospace; position: relative; margin: 10px 0;">
                
                    <p style="font-style: italic; line-height: 1.6;">
                        Dear Elaine,
                        <br/><br/>
                        I'm looking forward to the day you will be reading this letter to me in person. 
                        I'm sure we will be wrong about many things, but not about the fact that you are 
                        an adorable smart girl.
                        <br/><br/>
                        I prepared this page on April 10-11, in 2025. I love your parents very much 
                        and I hope you inherit (no pressure!) a lot from them.
                        <br/><br/>
                        With love,<br/>
                        Uncle Arthur
                    </p>
                
                    <div style="text-align: right; margin-top: 10px;">
                        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" 
                                  fill="#ff8f00" opacity="0.7"/>
                        </svg>
                    </div>
                </div>
                """
            },
        )
    
        # Return the accordion component
        return accordion

    # Create the accordion component
    letter_accordion = create_accordion_message()

    return (letter_accordion,)


@app.cell(hide_code=True)
def _(mo):
    # Create a letter for the parents inside an accordion

    def create_parents_letter_accordion():
        # Create the accordion with the letter inside
        accordion = mo.accordion(
            {
                "A Letter for Brandon & Lindsay ": f"""
                <div style="background-color: #e3f2fd; border-radius: 8px; padding: 25px; border: 1px solid #bbdefb; 
                      font-family: 'Georgia', serif; position: relative;
                      margin: 10px 0;">
                
                    <p style="line-height: 1.6; font-size: 1.05em;">
                        Hey,
                        <br/><br/>
                        I prepared this as a gift to Elaine and, of course, to you. This is a list of advice on how to raise a child from 0 to 10. 
                        Of course I know nothing about this and used deep research, which usually provides solid information.
                        <br/><br/>
                        Besides a cursory review, I haven't verified the quality of the results. They look solid and logical. 
                        They are, however, presented as hopeful goals rather than guarantees - aspirations for what we want to happen 
                        in a child's development. In any case, in the face of the unknown and absence of tested knowledge, 
                        logic is all we have.
                        <br/><br/>
                        With love,<br/>
                        Arthur
                    </p>
                
                    <div style="text-align: right; margin-top: 10px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" 
                                  fill="#1976d2" opacity="0.8"/>
                        </svg>
                    </div>
                </div>
                """
            },
        )
    
        # Return the accordion component
        return accordion

    # Create and display the parents letter accordion
    parents_letter_accordion = create_parents_letter_accordion()

    return (parents_letter_accordion,)


@app.cell(hide_code=True)
def _(letter_accordion, mo, parents_letter_accordion):

    # Display the accordion with a headline
    mo.output.replace(mo.vstack([
        parents_letter_accordion,
        letter_accordion,
    ]))
    return


@app.cell(hide_code=True)
def _():
    # Emojis for the advice tabs (ensure at least 5)
    advice_emojis = ["⭐", "🧸", "🎈", "🖍️", "💡"]

    # Corresponding styles for each advice tab content
    # Each item is a dict: {'border': 'border-color', 'bg': 'background-color'}
    advice_styles = [
        {'border': '#4285f4', 'bg': '#e8f0fe'}, # Blue
        {'border': '#34a853', 'bg': '#e6f4ea'}, # Green
        {'border': '#fbbc05', 'bg': '#fff8e1'}, # Yellow
        {'border': '#ea4335', 'bg': '#fce8e6'}, # Red
        {'border': '#9c27b0', 'bg': '#f3e5f5'}  # Purple
    ]

    year_value_map = {
        0: "Elaine is here! 🌱",
        1: "My first year! 🎂",
        2: "Toddler Times Two! 👣",
        3: "Happy three! ✨",
        4: "Fabulous Four! 🚀",
        5: "A full hand of years! 🖐️",
        6: "Super Six! 🦸",
        7: "Lucky Seven! 🍀",
        8: "I'm 8! I'm not a child!",
        9: "Nearly Double Digits! 🎉",
        10: "Two full hands! 🙌"
    }

    # Dictionary to store SVG content for each year
    flower_svgs = {
        0: """
        <!-- Replace with your Year 0 SVG code -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
            <!-- Background -->
            <rect width="400" height="300" fill="#e8f4f8"/>

            <!-- Ground -->
            <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>

            <!-- Snow patches -->
            <path d="M50,245 Q100,240 150,245 Q200,250 250,245 Q300,240 350,245 L350,250 L50,250 Z" fill="#f5f5f5" opacity="0.7"/>

            <!-- Wet soil crack -->
            <path d="M190,245 C193,240 190,235 195,230 C200,225 198,220 200,215" stroke="#3e2723" stroke-width="2" fill="none"/>
            <path d="M192,243 C195,238 192,233 197,228 C202,223 200,218 202,213" stroke="#3e2723" stroke-width="1.5" fill="none"/>

            <!-- Wet area around crack -->
            <ellipse cx="195" cy="240" rx="15" ry="5" fill="#5d4037" opacity="0.6"/>

            <!-- Water droplets -->
            <circle cx="197" cy="232" r="1.5" fill="#bbdefb"/>
            <circle cx="193" cy="237" r="1" fill="#bbdefb"/>
            <circle cx="199" cy="228" r="1" fill="#bbdefb"/>

            <!-- Tiny green sprout hint -->
            <path d="M200,245 C200,242 199,238 200,235" stroke="#81c784" stroke-width="0.8" fill="none"/>

            <!-- Melting snow particles -->
            <circle cx="180" cy="245" r="2" fill="white" opacity="0.8"/>
            <circle cx="210" cy="246" r="1.5" fill="white" opacity="0.7"/>
            <circle cx="175" cy="248" r="1" fill="white" opacity="0.6"/>
            <circle cx="215" cy="247" r="1" fill="white" opacity="0.5"/>
        </svg>
        """,

        1: """
        <!-- Replace with your Year 1 SVG code -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
            <!-- Background -->
            <rect width="400" height="300" fill="#e8f4f8"/>

            <!-- Ground -->
            <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>

            <!-- Tiny sprout -->
            <path d="M200,250 C199,240 201,235 200,225" stroke="#66bb6a" stroke-width="2" fill="none"/>

            <!-- First two tiny leaves -->
            <path d="M200,235 C195,233 190,235 195,238 C200,241 205,238 200,235" fill="#81c784" stroke="#66bb6a" stroke-width="0.8"/>
            <path d="M200,235 C205,233 210,235 205,238 C200,241 195,238 200,235" fill="#81c784" stroke="#66bb6a" stroke-width="0.8"/>

            <!-- Moist soil around sprout -->
            <ellipse cx="200" cy="250" rx="20" ry="5" fill="#5d4037" opacity="0.5"/>

            <!-- The diminishing crack -->
            <path d="M195,250 C197,245 196,240 198,238" stroke="#3e2723" stroke-width="1" fill="none" opacity="0.7"/>

            <!-- Dew drops -->
            <circle cx="201" cy="232" r="1" fill="#bbdefb" opacity="0.9"/>
            <circle cx="199" cy="237" r="0.8" fill="#bbdefb" opacity="0.8"/>
            <circle cx="203" cy="235" r="0.6" fill="#bbdefb" opacity="0.7"/>

            <!-- Small root hint -->
            <path d="M200,250 C198,255 202,260 199,265" stroke="#8d6e63" stroke-width="0.8" fill="none" opacity="0.5"/>
            <path d="M200,250 C202,255 198,260 201,265" stroke="#8d6e63" stroke-width="0.8" fill="none" opacity="0.5"/>
        </svg>
        """,

        # Add more years (2-10) with the corresponding SVG code
        # The pattern continues for years 2-10
        # Example for year 2:
        2: """
        <!-- Replace with your Year 2 SVG code -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
            <!-- Background -->
            <rect width="400" height="300" fill="#e8f4f8"/>

            <!-- Ground -->
            <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>

            <!-- Small stem -->
            <path d="M200,250 C198,240 202,230 200,220" stroke="#66bb6a" stroke-width="2.5" fill="none"/>

            <!-- First pair of true leaves -->
            <path d="M200,230 C190,228 180,230 185,235 C190,240 198,238 200,230" fill="#7cb342" stroke="#66bb6a" stroke-width="1"/>
            <path d="M200,230 C210,228 220,230 215,235 C210,240 202,238 200,230" fill="#7cb342" stroke="#66bb6a" stroke-width="1"/>

            <!-- Second smaller pair of leaves forming -->
            <path d="M200,220 C196,218 192,219 195,222 C198,225 202,222 200,220" fill="#81c784" stroke="#66bb6a" stroke-width="0.8"/>
            <path d="M200,220 C204,218 208,219 205,222 C202,225 198,222 200,220" fill="#81c784" stroke="#66bb6a" stroke-width="0.8"/>

            <!-- Moist soil -->
            <ellipse cx="200" cy="250" rx="25" ry="5" fill="#5d4037" opacity="0.4"/>

            <!-- Root system hints -->
            <path d="M200,250 C195,260 190,265 185,270" stroke="#8d6e63" stroke-width="1" fill="none" opacity="0.4"/>
            <path d="M200,250 C205,260 210,265 215,270" stroke="#8d6e63" stroke-width="1" fill="none" opacity="0.4"/>
        </svg>
        """,
        3: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Growing stem -->
          <path d="M200,250 C197,235 203,225 198,210 C195,195 202,185 200,175" stroke="#4caf50" stroke-width="3" fill="none"/>
      
          <!-- First set of mature leaves -->
          <path d="M198,230 C183,225 173,230 178,238 C183,246 193,240 198,230" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M202,230 C217,225 227,230 222,238 C217,246 207,240 202,230" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Second set of leaves -->
          <path d="M195,210 C180,205 170,210 175,218 C180,226 190,220 195,210" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M205,210 C220,205 230,210 225,218 C220,226 210,220 205,210" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Third new set of leaves forming -->
          <path d="M197,190 C190,186 182,188 187,194 C192,200 197,195 197,190" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
          <path d="M203,190 C210,186 218,188 213,194 C208,200 203,195 203,190" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
      
          <!-- Tiny bud beginning at top -->
          <circle cx="200" cy="175" r="3" fill="#f8bbd0" stroke="#ec407a" stroke-width="0.8"/>
      
          <!-- Dew drops -->
          <circle cx="183" cy="234" r="1.2" fill="#bbdefb" opacity="0.7"/>
          <circle cx="217" cy="234" r="1" fill="#bbdefb" opacity="0.6"/>
          <circle cx="180" cy="214" r="1.2" fill="#bbdefb" opacity="0.7"/>
          <circle cx="220" cy="214" r="1" fill="#bbdefb" opacity="0.6"/>
          <circle cx="200" cy="175" r="0.8" fill="#bbdefb" opacity="0.9"/>
        </svg>
        """,
        4: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Taller stem with slight curves -->
          <path d="M200,250 C197,230 203,220 198,200 C195,180 203,160 200,140" stroke="#4caf50" stroke-width="3.5" fill="none"/>
      
          <!-- Multiple leaf pairs down the stem -->
          <path d="M198,230 C183,225 173,230 178,238 C183,246 193,240 198,230" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M202,230 C217,225 227,230 222,238 C217,246 207,240 202,230" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <path d="M195,210 C180,205 170,210 175,218 C180,226 190,220 195,210" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M205,210 C220,205 230,210 225,218 C220,226 210,220 205,210" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <path d="M197,190 C182,185 172,190 177,198 C182,206 192,200 197,190" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M203,190 C218,185 228,190 223,198 C218,206 208,200 203,190" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <path d="M195,170 C180,165 175,170 180,178 C185,186 190,180 195,170" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M205,170 C220,165 225,170 220,178 C215,186 210,180 205,170" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Developing bud -->
          <ellipse cx="200" cy="140" rx="8" ry="12" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
      
          <!-- Sepal formation beginning -->
          <path d="M192,145 C188,140 186,135 190,138" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
          <path d="M208,145 C212,140 214,135 210,138" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
          <path d="M196,152 C194,158 192,163 196,160" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
          <path d="M204,152 C206,158 208,163 204,160" fill="#81c784" stroke="#4caf50" stroke-width="0.8"/>
      
          <!-- Morning dew -->
          <circle cx="193" cy="143" r="1" fill="#bbdefb" opacity="0.8"/>
          <circle cx="207" cy="143" r="1" fill="#bbdefb" opacity="0.8"/>
          <circle cx="200" cy="132" r="0.8" fill="#bbdefb" opacity="0.9"/>
        </svg>
        """,
        5: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Stem -->
          <path d="M200,250 C198,220 202,210 198,180 C195,150 205,130 200,100" stroke="#4caf50" stroke-width="4" fill="none"/>
      
          <!-- Small leaf left -->
          <path d="M198,220 C185,215 175,218 180,225 C185,232 195,228 198,220" fill="#81c784" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Small leaf right -->
          <path d="M202,190 C215,185 225,188 220,195 C215,202 205,198 202,190" fill="#81c784" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Medium leaf left -->
          <path d="M195,160 C175,155 165,160 175,170 C185,180 190,175 195,160" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Closed flower bud -->
          <ellipse cx="200" cy="100" rx="15" ry="25" fill="#f8bbd0" stroke="#ec407a" stroke-width="1.5"/>
      
          <!-- Sepal elements -->
          <path d="M185,110 C180,95 185,85 190,95" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M215,110 C220,95 215,85 210,95" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M195,125 C185,130 182,140 192,135" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
          <path d="M205,125 C215,130 218,140 208,135" fill="#66bb6a" stroke="#4caf50" stroke-width="1"/>
      
          <!-- Bud structure lines -->
          <path d="M195,100 C197,90 203,90 205,100" stroke="#f48fb1" stroke-width="1" fill="none"/>
          <path d="M190,100 C195,85 205,85 210,100" stroke="#f48fb1" stroke-width="0.8" fill="none" opacity="0.6"/>
          <path d="M200,75 L200,100" stroke="#f48fb1" stroke-width="0.8" fill="none" opacity="0.6"/>
      
          <!-- Dew drops -->
          <circle cx="188" cy="108" r="1.5" fill="#bbdefb" opacity="0.8"/>
          <circle cx="212" cy="107" r="1.3" fill="#bbdefb" opacity="0.7"/>
          <circle cx="200" cy="78" r="1" fill="#bbdefb" opacity="0.9"/>
        </svg>
        """,
        6: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Stem growth between year 5 and 6 -->
          <path d="M200,250 C197,220 203,200 197,180 C194,160 206,140 200,100" stroke="#2e7d32" stroke-width="4" fill="none"/>
      
          <!-- Multiple leaf pairs -->
          <path d="M197,225 C177,220 167,225 172,235 C177,245 187,240 197,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M203,225 C223,220 233,225 228,235 C223,245 213,240 203,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M194,200 C174,195 164,200 169,210 C174,220 184,215 194,200" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M206,200 C226,195 236,200 231,210 C226,220 216,215 206,200" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M196,175 C176,170 166,175 171,185 C176,195 186,190 196,175" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M204,175 C224,170 234,175 229,185 C224,195 214,190 204,175" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M193,150 C173,145 163,150 168,160 C173,170 183,165 193,150" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M207,150 C227,145 237,150 232,160 C227,170 217,165 207,150" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M197,125 C177,120 167,125 172,135 C177,145 187,140 197,125" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M203,125 C223,120 233,125 228,135 C223,145 213,140 203,125" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <!-- Maturing bud - transitioning between year 5 and 6 -->
          <ellipse cx="200" cy="100" rx="16" ry="28" fill="#f8bbd0" stroke="#ec407a" stroke-width="1.5"/>
      
          <!-- Sepals slightly more developed than year 5 but not yet like year 6 -->
          <path d="M184,110 C174,100 169,90 179,100" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M216,110 C226,100 231,90 221,100" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M184,90 C174,80 169,70 179,80" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M216,90 C226,80 231,70 221,80" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M192,128 C182,138 177,148 187,138" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M208,128 C218,138 223,148 213,138" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
      
          <!-- Beginning of color differentiation in the bud -->
          <path d="M195,100 C198,90 202,90 205,100" stroke="#f48fb1" stroke-width="1.2" fill="none"/>
          <path d="M190,100 C195,85 205,85 210,100" stroke="#f48fb1" stroke-width="1" fill="none" opacity="0.7"/>
          <path d="M200,72 L200,100" stroke="#f48fb1" stroke-width="1" fill="none" opacity="0.7"/>
      
          <!-- New feature: slight hints of petals starting to form inside -->
          <path d="M197,85 C195,80 198,75 200,80" stroke="#f06292" stroke-width="0.8" fill="none" opacity="0.6"/>
          <path d="M203,85 C205,80 202,75 200,80" stroke="#f06292" stroke-width="0.8" fill="none" opacity="0.6"/>
      
          <!-- Morning dew -->
          <circle cx="184" cy="104" r="1.5" fill="#bbdefb" opacity="0.8"/>
          <circle cx="216" cy="104" r="1.3" fill="#bbdefb" opacity="0.7"/>
          <circle cx="200" cy="74" r="1" fill="#bbdefb" opacity="0.9"/>
      
          <!-- Subtle glow indicating coming transformation -->
          <ellipse cx="200" cy="100" rx="22" ry="34" fill="white" opacity="0.15" filter="blur(5px)"/>
        </svg>
        """,
        7: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Stronger stem -->
          <path d="M200,250 C196,225 204,200 196,175 C192,150 208,125 200,95" stroke="#2e7d32" stroke-width="4.5" fill="none"/>
      
          <!-- Multiple leaf pairs -->
          <path d="M196,225 C176,220 166,225 171,235 C176,245 186,240 196,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M204,225 C224,220 234,225 229,235 C224,245 214,240 204,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M193,200 C173,195 163,200 168,210 C173,220 183,215 193,200" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M207,200 C227,195 237,200 232,210 C227,220 217,215 207,200" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M195,175 C175,170 165,175 170,185 C175,195 185,190 195,175" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M205,175 C225,170 235,175 230,185 C225,195 215,190 205,175" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M192,150 C172,145 162,150 167,160 C172,170 182,165 192,150" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M208,150 C228,145 238,150 233,160 C228,170 218,165 208,150" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <path d="M196,125 C176,120 166,125 171,135 C176,145 186,140 196,125" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
          <path d="M204,125 C224,120 234,125 229,135 C224,145 214,140 204,125" fill="#388e3c" stroke="#2e7d32" stroke-width="1.2"/>
      
          <!-- Maturing bud -->
          <ellipse cx="200" cy="95" rx="18" ry="30" fill="#f8bbd0" stroke="#ec407a" stroke-width="1.5"/>
      
          <!-- Fully formed sepals -->
          <path d="M182,105 C172,95 167,85 177,95" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M218,105 C228,95 233,85 223,95" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M190,125 C180,135 175,145 185,135" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
          <path d="M210,125 C220,135 225,145 215,135" fill="#66bb6a" stroke="#388e3c" stroke-width="1.2"/>
      
          <!-- Internal bud structure hints -->
          <path d="M195,95 C200,85 200,75 205,95" stroke="#f48fb1" stroke-width="1" fill="none"/>
          <path d="M190,95 C200,80 200,70 210,95" stroke="#f48fb1" stroke-width="0.8" fill="none" opacity="0.6"/>
          <path d="M200,65 L200,95" stroke="#f48fb1" stroke-width="0.8" fill="none" opacity="0.6"/>
      
          <!-- Morning dew -->
          <circle cx="182" cy="100" r="1.5" fill="#bbdefb" opacity="0.8"/>
          <circle cx="218" cy="100" r="1.3" fill="#bbdefb" opacity="0.7"/>
          <circle cx="200" cy="68" r="1" fill="#bbdefb" opacity="0.9"/>
        </svg>
        """,
        8: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Stronger stem with character -->
          <path d="M200,250 C195,220 205,195 195,170 C190,145 205,120 198,95 C195,80 202,75 200,60" stroke="#2e7d32" stroke-width="5" fill="none"/>
      
          <!-- Rich foliage - multiple leaf pairs -->
          <path d="M196,225 C176,220 161,230 171,240 C181,250 186,240 196,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M204,225 C224,220 239,230 229,240 C219,250 214,240 204,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M193,195 C173,190 158,200 168,210 C178,220 183,210 193,195" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M207,195 C227,190 242,200 232,210 C222,220 217,210 207,195" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M190,165 C170,160 155,170 165,180 C175,190 180,180 190,165" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M210,165 C230,160 245,170 235,180 C225,190 220,180 210,165" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M193,135 C173,130 158,140 168,150 C178,160 183,150 193,135" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M207,135 C227,130 242,140 232,150 C222,160 217,150 207,135" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M195,105 C175,100 160,110 170,120 C180,130 185,120 195,105" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M205,105 C225,100 240,110 230,120 C220,130 215,120 205,105" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <!-- Mature bud with sepals beginning to part slightly -->
          <ellipse cx="200" cy="60" rx="20" ry="32" fill="#f8bbd0" stroke="#ec407a" stroke-width="1.5"/>
      
          <!-- Sepals starting to separate -->
          <path d="M180,70 C165,60 155,65 165,75 C175,85 175,75 180,70" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M220,70 C235,60 245,65 235,75 C225,85 225,75 220,70" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M180,50 C165,40 155,45 165,55 C175,65 175,55 180,50" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M220,50 C235,40 245,45 235,55 C225,65 225,55 220,50" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M190,90 C175,100 165,105 175,95 C185,85 185,95 190,90" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M210,90 C225,100 235,105 225,95 C215,85 215,95 210,90" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
      
          <!-- Tiny glimpse of pink petals between sepals -->
          <path d="M199,45 C195,40 198,35 201,40 C204,45 201,40 199,45" fill="#f06292" stroke="#ec407a" stroke-width="0.8"/>
          <path d="M201,45 C205,40 202,35 199,40 C196,45 199,40 201,45" fill="#f06292" stroke="#ec407a" stroke-width="0.8"/>
      
          <!-- Internal bud structure hints -->
          <path d="M195,60 C200,50 200,40 205,60" stroke="#f48fb1" stroke-width="1" fill="none"/>
          <path d="M190,60 C200,45 200,35 210,60" stroke="#f48fb1" stroke-width="0.8" fill="none" opacity="0.7"/>
      
          <!-- Morning dew -->
          <circle cx="175" cy="65" r="1.5" fill="#bbdefb" opacity="0.8"/>
          <circle cx="225" cy="65" r="1.3" fill="#bbdefb" opacity="0.7"/>
          <circle cx="198" cy="38" r="1" fill="#bbdefb" opacity="0.9"/>
          <circle cx="202" cy="38" r="0.8" fill="#bbdefb" opacity="0.8"/>
        </svg>
        """,
        9: """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
          <!-- Background -->
          <rect width="400" height="300" fill="#e8f4f8"/>
      
          <!-- Ground -->
          <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>
      
          <!-- Strong mature stem -->
          <path d="M200,250 C195,220 205,195 195,170 C190,145 205,120 198,95 C195,75 205,60 200,40" stroke="#2e7d32" stroke-width="5" fill="none"/>
      
          <!-- Full foliage -->
          <path d="M196,225 C170,218 155,230 170,245 C185,260 191,250 196,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M204,225 C230,218 245,230 230,245 C215,260 209,250 204,225" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M193,195 C167,188 152,200 167,215 C182,230 188,220 193,195" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M207,195 C233,188 248,200 233,215 C218,230 212,220 207,195" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M190,165 C164,158 149,170 164,185 C179,200 185,190 190,165" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M210,165 C236,158 251,170 236,185 C221,200 215,190 210,165" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M193,135 C167,128 152,140 167,155 C182,170 188,160 193,135" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M207,135 C233,128 248,140 233,155 C218,170 212,160 207,135" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M195,105 C169,98 154,110 169,125 C184,140 190,130 195,105" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M205,105 C231,98 246,110 231,125 C216,140 210,130 205,105" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <path d="M197,75 C171,68 161,80 176,90 C191,100 192,90 197,75" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
          <path d="M203,75 C229,68 239,80 224,90 C209,100 208,90 203,75" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
      
          <!-- Bud with sepals clearly opening -->
          <ellipse cx="200" cy="40" rx="22" ry="30" fill="#f8bbd0" stroke="#ec407a" stroke-width="1.5"/>
      
          <!-- Sepals distinctly pulled back -->
          <path d="M178,50 C163,40 153,45 163,55 C173,65 173,60 178,50" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M222,50 C237,40 247,45 237,55 C227,65 227,60 222,50" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M178,35 C163,25 153,30 163,40 C173,50 173,45 178,35" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M222,35 C237,25 247,30 237,40 C227,50 227,45 222,35" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M185,65 C170,75 160,80 170,70 C180,60 180,55 185,65" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
          <path d="M215,65 C230,75 240,80 230,70 C220,60 220,55 215,65" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
      
          <!-- Pink petals visible but still tightly closed -->
          <path d="M200,40 C195,30 190,20 195,15 C200,10 205,15 200,40" fill="#f06292" stroke="#ec407a" stroke-width="1"/>
          <path d="M200,40 C205,30 210,20 205,15 C200,10 195,15 200,40" fill="#f06292" stroke="#ec407a" stroke-width="1"/>
          <path d="M200,40 C190,35 180,25 185,20 C190,15 200,20 200,40" fill="#f06292" stroke="#ec407a" stroke-width="1"/>
          <path d="M200,40 C210,35 220,25 215,20 C210,15 200,20 200,40" fill="#f06292" stroke="#ec407a" stroke-width="1"/>
      
          <!-- Flower center starting to form -->
          <circle cx="200" cy="40" r="5" fill="#f8bbd0"/>
      
          <!-- Morning dew -->
          <circle cx="170" cy="45" r="1.5" fill="#bbdefb" opacity="0.8"/>
          <circle cx="230" cy="45" r="1.3" fill="#bbdefb" opacity="0.7"/>
          <circle cx="195" cy="15" r="1" fill="#bbdefb" opacity="0.9"/>
          <circle cx="205" cy="15" r="0.8" fill="#bbdefb" opacity="0.8"/>
        </svg>
        """,

        # Continue with years 3-10...
        # For brevity, I'll add placeholders for years 3-9 and include year 10

        10: """
        <!-- Replace with your Year 10 SVG code -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
            <!-- Background -->
            <rect width="400" height="300" fill="#e8f4f8"/>

            <!-- Ground -->
            <path d="M0,250 L400,250 L400,300 L0,300 Z" fill="#6d4c41"/>

            <!-- Strong stem -->
            <path d="M200,250 C197,230 203,210 197,190 C192,170 208,150 203,130 C198,110 202,90 200,70" stroke="#2e7d32" stroke-width="5" fill="none"/>

            <!-- Leaves -->
            <path d="M197,220 C175,215 160,225 175,235 C190,245 195,235 197,220" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
            <path d="M203,190 C225,180 235,195 220,205 C205,215 200,200 203,190" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
            <path d="M192,160 C170,155 155,170 170,180 C185,190 188,175 192,160" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>
            <path d="M208,130 C230,125 240,140 225,150 C210,160 205,145 208,130" fill="#388e3c" stroke="#2e7d32" stroke-width="1.5"/>

            <!-- Flower just beginning to open -->
            <!-- Sepals -->
            <path d="M185,80 C175,70 165,80 175,90 C185,100 185,90 185,80" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
            <path d="M215,80 C225,70 235,80 225,90 C215,100 215,90 215,80" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
            <path d="M185,60 C175,50 165,60 175,70 C185,80 185,70 185,60" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>
            <path d="M215,60 C225,50 235,60 225,70 C215,80 215,70 215,60" fill="#66bb6a" stroke="#388e3c" stroke-width="1.5"/>

            <!-- Petals just starting to open -->
            <path d="M200,70 C185,60 175,45 185,35 C195,25 205,35 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
            <path d="M200,70 C215,60 225,45 215,35 C205,25 195,35 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
            <path d="M200,70 C195,55 180,40 190,30 C200,20 210,30 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
            <path d="M200,70 C205,55 220,40 210,30 C200,20 190,30 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
            <path d="M200,70 C190,55 175,50 180,35 C185,20 200,25 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>
            <path d="M200,70 C210,55 225,50 220,35 C215,20 200,25 200,70" fill="#f8bbd0" stroke="#ec407a" stroke-width="1"/>

            <!-- Flower center -->
            <circle cx="200" cy="70" r="10" fill="#ffeb3b"/>
            <circle cx="200" cy="70" r="7" fill="#ffc107"/>
        </svg>
        """
    }

    # Dictionary to store advice for each year
    parenting_advice = {
        0: [
            "Respond consistently to distress, but avoid hyper-attunement to every minor fuss; allow brief moments for infant self-discovery/soothing within a secure context.",
            "Aim for one consistent primary caregiver, especially in the first 6 months, to provide a clear anchor for secure attachment, more so than a patchwork of caregivers.",
            "Look beyond crying; recognize signs of overstimulation (gaze aversion, arching) and other non-verbal cues to provide more attuned care and prevent meltdowns.",
            "During inconsolable crying, focus on providing a calm, steady, regulating presence (\"containment\") rather than solely on stopping the tears immediately.",
            "Reserve firm \"No's\" for safety; use quick, engaging redirection for most non-dangerous exploration to respect developmental drives while maintaining boundaries."
        ],

        1: [
            "Proactively build tolerance for separation through games (peek-a-boo, hide-and-seek with talking) and short, planned practice separations, not just reacting to anxiety.",
            "Never sneak out; use a brief, consistent ritual and leave confidently (even with tears) stating return time concretely. Lingering prolongs distress.",
            "Go beyond responding; expand toddler's utterance into a full phrase, then extend the topic with new info or questions to accelerate language skills.",
            "Frame participation in routines (dressing, cleanup) as helpful contributions, leveraging imitation drive to foster competence and cooperation, not just compliance.",
            "View \"No!\" and boundary testing primarily as cognitive exploration (cause/effect, autonomy), not just defiance, allowing for more empathetic limit-setting."
        ],

        2: [
            "Use tantrums as teaching moments: systematically validate feelings, label emotions, connect, and set limits while problem-solving, turning conflict into connection.",
            "Reframe tantrums not as manipulation, but as communication of overwhelm or testing control; respond calmly, acknowledge desire, hold limits, comfort after.",
            "During meltdowns, focus first on helping the child calm down using your own calm presence before attempting to correct behavior or teach lessons.",
            "If a break is needed, use a calm-down space with or near the child, focusing on regulation support, not punitive isolation which can increase shame/distress.",
            "Go beyond basic labels; introduce nuanced feeling words in context and use a simple color-based Mood Meter to help toddlers categorize and express emotions."
        ],

        3: [
            "Strategically use imaginative play scenarios (with dolls, puppets) to practice challenging social skills like sharing, turn-taking, and conflict resolution.",
            "Go beyond \"calm down\"; teach concrete methods like \"belly breathing,\" using a calm-down space/jar, or visual aids, and practice them during calm times.",
            "Make transitions smoother by pairing verbal warnings (e.g., \"5 more minutes\") with a sensory cue like a visual timer, a specific song, or a gentle touch.",
            "Actively teach emotion recognition using games with feeling face cards, discussing character expressions in books, and labeling emotions observed in others.",
            "Emphasize effort over outcome in praise; when misbehavior occurs, focus on understanding impact and \"repairing\" harm (apology, kind deed) rather than solely on punishment."
        ],

        4: [
            "Allow small, safe failures and manageable risks; don't rescue from all challenges. Frame setbacks as learning opportunities to build coping skills and perseverance.",
            "Go beyond encouragement; teach a concrete process (Stop/Calm, Say Problem, Think Solutions, Try, Reflect) for navigating conflicts and challenges.",
            "To promote reflection and solutions instead of defensiveness, ask \"How can you fix this?\" or \"What could you do differently?\" instead of \"Why did you do that?\".",
            "Frame chores and helpful behaviors not just as tasks, but as contributions that care for the family, pets, or shared spaces, linking responsibility to empathy.",
            "Acknowledge anxiety (\"It's okay to feel scared\"), but gently coach facing fears in small steps rather than allowing complete avoidance, which reinforces anxiety."
        ],

        5: [
            "Deliberately resist correcting imperfect efforts on self-care tasks (crooked bed-making, misaligned buttons) to prioritize developing intrinsic motivation and competence over perfectionism, especially challenging for achievement-oriented parents.", "Invest in robust imaginative play that develops classroom-essential social-emotional skills (turn-taking, rule-following, negotiating roles) rather than primarily drilling academic readiness like letter recognition.", "Anchor abstract time words ('tomorrow,' 'later') to concrete sequential experiences ('after you sleep, wake up, and eat breakfast') to reduce confusion and anxiety about anticipated events.", "Recognize 'talking back' as often representing clumsy bids for autonomy; acknowledge the underlying need for independence while redirecting to appropriate expressions by offering legitimate choices.", "Transform storytime into proactive social-emotional training by posing questions that prompt problem-solving: 'What could the character have done instead?' to mentally rehearse strategies for navigating school social scenarios."

        ],

        6: [
            "Deliberately shift praise from outcomes or innate traits ('You're so smart!') to process and strategy ('You found a clever way to solve that problem'), which research shows builds resilience, challenge-seeking, and a growth mindset.", "Explicitly teach friendship initiation skills through role-play (joining groups, sharing materials/ideas, being a good listener) rather than assuming social competencies develop naturally without direct instruction.", "Frame household rules through the lens of fairness and logical consequences ('We clean toys so everyone has safe play space') rather than authority alone, leveraging six-year-olds' emerging sense of justice and cause-effect reasoning.", "Introduce 'feeling thermometers' (1-5 scales) to help children develop emotional granularity beyond basic labels, teaching that different intensity levels require different regulation strategies.", "Deliberately schedule periods of unstructured 'do nothing' time (distinct from screen time) where boredom becomes the catalyst for creativity, daydreaming, and developing internal resources, especially valuable for children with highly scheduled lives."
        ],

        7: [
            "Present hypothetical social dilemmas during calm moments ('What would you do if you saw someone sitting alone?') to actively cultivate perspective-taking skills that build on seven-year-olds' emerging empathy.", "When addressing lying, recognize it partially as evidence of cognitive development (Theory of Mind), respond calmly without high emotion, and focus conversations on trust and relationship rather than punishment.", "Replace ineffective reassurances about fears ('Don't worry') with validation plus collaborative coping strategies ('It's normal to feel nervous; let's create a plan together with specific steps to manage this situation').", "During disagreements, explicitly introduce the concept that two people can experience the same event differently and both perspectives can be valid, challenging their tendency toward single-factor thinking.", "Elevate reading practice beyond decoding to 'meaning detective' work by asking questions about character motivation, multiple word meanings, and contextual clues about emotions not explicitly stated in text."
        ],

        8: [
            "Proactively rehearse specific peer pressure resistance techniques through role-play (direct refusal, suggesting alternatives, having exit strategies) rather than simply warning about 'bad influences' or expecting good choices without practice.", "Reframe emotional outbursts as evidence of lagging skills (emotional regulation, impulse control) rather than pure misbehavior, responding with empathy for the feeling, clear boundaries on behavior, then explicitly teaching missing coping strategies.", "Support exploration of varying interests without excessive pressure for long-term commitment, recognizing that dabbling and shifting passions are fundamental to self-discovery rather than signs of problematic inconsistency.", "Leverage eight-year-olds' black-and-white thinking to establish clear family values ('In our family, we tell the truth even when it's difficult'), providing moral foundations that will guide more complex ethical reasoning later.", "Implement the 'complaint sandwich' technique when children express criticism rudely: validate the underlying feeling, set clear boundaries about respectful communication, then suggest alternative phrasing that addresses the same concern appropriately."
        ],

        9: [
            "Shift from solving your child's problems to collaborative brainstorming by asking guiding questions ('What solutions have you considered?' 'What else might work?') that position you as consultant rather than fixer, building resourcefulness and problem-solving confidence.", "Complement screen time limits with active 'digital citizenship' education covering online safety, respectful communication, privacy management, information evaluation, and understanding the permanence of digital footprints.", "Initiate factual, matter-of-fact conversations about puberty before significant physical changes occur, using age-appropriate books and language to normalize the process and establish yourself as a trusted information source.", "Consciously model healthy conflict resolution between parents using 'I feel' statements, focusing on needs not blame, and working toward solutions, providing your child a lived blueprint for managing her own complex social relationships.", "Frame household responsibilities as contributions to family functioning ('we all help our home run smoothly') rather than tying basic chores directly to allowance, which can inadvertently create a purely transactional view of family participation."
        ],

        10: [
            "Evolve from 'rules enforcer' to 'values consultant' by asking questions that help your preteen apply core family principles to complex situations ('How does our value of kindness apply to this friendship dilemma?'), developing internal moral reasoning.", "Move beyond content filtering to actively teaching media literacy skills by discussing who creates media messages and why, identifying stereotypes (particularly gender-based ones), distinguishing fact from opinion, and analyzing persuasion techniques.", "Establish simple but consistent one-on-one connection rituals (bedtime chats, weekly walks, shared hobbies) that signal ongoing availability despite busy schedules and your child's natural gravitational pull toward peer relationships.", "Nurture healthy skepticism by encouraging your child to respectfully question assumptions, look for supporting evidence, and think critically about information, framing this as valuable intellectual development rather than defiance.", "Deliberately shift body-related conversations away from appearance toward function and capability ('bodies are for doing, not just for looking'), emphasizing strength, energy, and health over weight, shape or conventional attractiveness."
        ]
    }

    return (
        advice_emojis,
        advice_styles,
        flower_svgs,
        parenting_advice,
        year_value_map,
    )


@app.cell(hide_code=True)
def _(year_value_map):
    # Create tab labels for years
    tab_labels = [f"Year {i}" for i in range(11)]

    # Create the year tabs widget - Keys are labels, values don't matter here
    # as the content is generated reactively in the next cell.
    tabs_dict_years = {}
    for i in range(11):
        label = f"Year {i}"
        # Get the custom value from the map, provide a fallback if needed
        value = year_value_map.get(i, f"Value for Year {i}")
        tabs_dict_years[label] = value


    return (tabs_dict_years,)


@app.cell(hide_code=True)
def _(mo, tabs_dict_years, year_value_map):
    default_year_value = year_value_map[0]
    year_tabs = mo.ui.tabs(tabs_dict_years, value=default_year_value)
    return (year_tabs,)


@app.cell(hide_code=True)
def _(advice_emojis, advice_styles, mo):
    def create_advice_tabs_dictionary(advice_list):
        """Creates the dictionary mapping advice tab emojis to styled content."""
        _advice_tabs_dict = {}
        if not advice_list:
            _advice_tabs_dict["Info"] = mo.md("No specific advice available for this year.")
        else:
            for i, advice_text in enumerate(advice_list):
                # Ensure we don't go out of bounds for emojis/styles
                if i < len(advice_emojis) and i < len(advice_styles):
                    tab_key = advice_emojis[i] # Use emoji as the key/label
                    current_style = advice_styles[i] # Get the style dict for this tip

                    advice_content = mo.md(f"""
                    <div style="background-color: {current_style['bg']}; border-radius: 5px; padding: 15px; border-left: 5px solid {current_style['border']}; min-height: 50px; display: flex; align-items: center;">
                        <p style="margin: 0; font-size: 1em; color: #333;">{advice_text}</p>
                    </div>
                    """)
                    _advice_tabs_dict[tab_key] = advice_content
                else:
                    # Fallback if there are more tips than emojis/styles (optional)
                    tab_key = f"Tip {i+1}"
                    advice_content = mo.md(f"<p>{advice_text}</p>") # Basic fallback
                    _advice_tabs_dict[tab_key] = advice_content

        return _advice_tabs_dict
    return (create_advice_tabs_dictionary,)


@app.cell(hide_code=True)
def _(year_tabs):
    selected_year_str = year_tabs.value.split()[-1]
    selected_year = int(selected_year_str)
    return (selected_year,)


@app.cell(hide_code=True)
def _(flower_svgs, mo, selected_year):
    # 1. Get the SVG for the selected year
    svg_display = mo.Html(f"""
    <div style="
        display: flex;
        justify-content: center; /* Center the content horizontally */
        padding: 20px 10px;      /* Add some vertical padding */
        margin: 15px 0;         /* Add margin above and below */
        background-color: #f8f9fa; /* Light background color */
        border-radius: 12px;       /* Rounded corners */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Subtle shadow */
        border: 1px solid #e9ecef; /* Light border */
    ">
        {flower_svgs.get(selected_year, "<!-- SVG not found -->")}
    </div>
    """)
    return (svg_display,)


@app.cell(hide_code=True)
def _(parenting_advice, selected_year):
    advice_list_for_year = parenting_advice.get(selected_year, [])

    return (advice_list_for_year,)


@app.cell(hide_code=True)
def _(advice_list_for_year, create_advice_tabs_dictionary):
    advice_tabs_dict = create_advice_tabs_dictionary(advice_list_for_year)

    return (advice_tabs_dict,)


@app.cell(hide_code=True)
def _(mo, year_tabs):
    show_years = mo.Html(f"""
    <div style="
        display: flex;
        justify-content: center; /* Center the tabs horizontally */
        padding: 20px 10px;      /* Add some vertical padding */
        margin: 15px 0;         /* Add margin above and below */
        background-color: #f8f9fa; /* Light background color */
        border-radius: 12px;       /* Rounded corners */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Subtle shadow */
        border: 1px solid #e9ecef; /* Light border */
    ">
        {year_tabs}
    </div>
    """)
    return (show_years,)


@app.cell(hide_code=True)
def _(advice_emojis, advice_list_for_year, advice_tabs_dict, mo):
    default_advice_tab = advice_emojis[0] if advice_list_for_year else "Info"
    individual_advice_tabs = mo.ui.tabs(advice_tabs_dict, value=default_advice_tab)
    return (individual_advice_tabs,)


@app.cell(hide_code=True)
def _(individual_advice_tabs, mo, show_years, svg_display):
    mo.vstack([
        mo.Html("""
    <div style="text-align: center; font-family: Garamond, serif; font-weight: bold; font-size: 1.5em;">
    A Letter to Elaine
    </div>
    """),
        show_years,
        svg_display,
        mo.md("---"),
        individual_advice_tabs
    ])
    return


@app.cell(hide_code=True)
def _(mo):

    # Final capsule with source link
    final_capsule = mo.Html(f"""
    <div style="
        background-color: #f0f0f0; /* Light grey background */
        border-radius: 15px;       /* Rounded corners */
        padding: 15px 25px;        /* Padding inside the capsule */
        margin: 25px auto;         /* Margin top/bottom and centered horizontally */
        text-align: center;        /* Center the text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
        font-size: 0.9em;          /* Slightly smaller font size */
        color: #555;               /* Dark grey text color */
        border: 1px solid #ddd;    /* Light border */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Subtle shadow */
        max-width: 800px;          /* Limit the width */
    ">
        Compiled sources: 
        <a href="https://docs.google.com/document/d/1PhMmoAAGtcYAsHW2TUWxdZ4rL_P85iCES-UnU_ZOp4Q/edit?usp=sharing" 
           target="_blank" 
           rel="noopener noreferrer"
           style="color: #007bff; text-decoration: none; font-weight: 500;"
           onmouseover="this.style.textDecoration='underline'"
           onmouseout="this.style.textDecoration='none'">
            Google Docs Link
        </a>
    </div>
    """)

    # Display the final capsule
    final_capsule
    return


if __name__ == "__main__":
    app.run()
