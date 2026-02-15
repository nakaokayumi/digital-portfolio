# digital-portfolio
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nakaoka Yumi | Cybersecurity Analyst</title>
    <script src="https://unpkg.com/typed.js@2.1.0/dist/typed.umd.js"></script>
    <style>
        :root {
            --bg-black: #050505;
            --card-bg: #0d0d0d;
            --grab-red: #cc0000;
            --text-gray: #a0a0a0;
            --neon-red: #ff3131;
            --terminal-green: #00ff41;
        }

        body {
            background-color: var(--bg-black);
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            overflow-x: hidden;
        }

        /* Navigation */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.2rem 8%;
            background: rgba(0,0,0,0.95);
            position: fixed;
            width: 84%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #1a1a1a;
        }

        nav .logo { color: var(--neon-red); font-weight: 900; letter-spacing: 2px; }
        nav a { color: white; text-decoration: none; margin-left: 25px; font-size: 0.8rem; letter-spacing: 1px; }
        nav a:hover { color: var(--neon-red); }

        /* Hero Section */
        header {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 0 10%;
            background: radial-gradient(circle at center, #1a0505 0%, #050505 100%);
        }

        .typing-container { font-family: 'Courier New', Courier, monospace; font-size: 1.5rem; color: var(--text-gray); height: 50px; }
        header h1 { font-size: 4.5rem; margin: 10px 0; color: white; }
        header h1 span { color: var(--neon-red); }

        /* Project Terminal Style */
        .terminal-window {
            background: #000;
            border: 1px solid #333;
            border-radius: 6px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-top: 40px;
        }

        .terminal-header {
            background: #1a1a1a;
            padding: 10px;
            display: flex;
            gap: 8px;
            border-radius: 6px 6px 0 0;
        }

        .dot { width: 12px; height: 12px; border-radius: 50%; }
        .red { background: #ff5f56; } .yellow { background: #ffbd2e; } .green { background: #27c93f; }

        .terminal-body { padding: 20px; font-family: 'Consolas', monospace; color: var(--terminal-green); }
        .command { color: #fff; }

        /* Sections */
        section { padding: 100px 10%; }
        h2 { color: var(--neon-red); text-transform: uppercase; font-size: 1.8rem; margin-bottom: 40px; border-bottom: 1px solid #222; display: inline-block; }

        .btn {
            background: transparent;
            color: var(--neon-red);
            border: 1px solid var(--neon-red);
            padding: 12px 30px;
            text-decoration: none;
            transition: 0.3s;
            display: inline-block;
            margin-top: 20px;
        }

        .btn:hover { background: var(--neon-red); color: white; box-shadow: 0 0 15px var(--neon-red); }
    </style>
</head>
<body>

    <nav>
        <div class="logo">YUMI // SEC</div>
        <div>
            <a href="#projects">PROJECTS</a>
            <a href="#experience">EXPERIENCE</a>
            <a href="#contact">CONTACT</a>
        </div>
    </nav>

    <header>
        <div class="typing-container">
            <span id="typed"></span>
        </div>
        <h1>NAKAOKA <span>YUMI</span></h1>
        <p style="max-width: 600px; color: var(--text-gray);">Cybersecurity & Digital Forensics student specializing in <strong>Identity Access Management</strong> and <strong>Incident Response</strong>. Audit-ready mindset with industrial QA experience.</p>
        <div>
            <a href="#projects" class="btn">INITIALIZE SEARCH</a>
        </div>
    </header>

    <section id="projects">
        <h2>./Featured_Project</h2>
        <div class="terminal-window">
            <div class="terminal-header">
                <div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div>
            </div>
            <div class="terminal-body">
                <p><span class="command">yumi@sec:~$</span> run analyze_project "Secure IAM Portal"</p>
                <p>> [STATUS] Analyzing Architecture...</p>
                <p>> [SEC] PBKDF2 Hashing: <span style="color:white">ENABLED</span></p>
                <p>> [SEC] SQLi Prevention: <span style="color:white">ACTIVE</span></p>
                <p>> [COMPLIANCE] PDPA Audit Logging: <span style="color:white">VERIFIED</span></p>
                <p style="color: var(--text-gray); margin-top: 20px;">Built with Python/Flask to demonstrate OWASP mitigation and session integrity for enterprise platforms like Grab.</p>
                <a href="https://github.com/nakaokayumi/secure-identity-portal" style="color: var(--neon-red); text-decoration: none;">[VIEW REPOSITORY]</a>
            </div>
        </div>
    </section>

    <script>
        var typed = new Typed('#typed', {
            strings: [
                'Establishing Secure Connection...',
                'Analyzing Attack Lifecycle...',
                'Mitigating OWASP Vulnerabilities...',
                'Ready for Deployment.'
            ],
            typeSpeed: 50,
            backSpeed: 30,
            loop: true
        });
    </script>

</body>
</html>
