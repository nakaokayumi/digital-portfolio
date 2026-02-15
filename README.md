# digital-portfolio
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nakaoka Yumi | Cybersecurity Portfolio</title>
    <style>
        :root {
            --bg-black: #0a0a0a;
            --card-bg: #141414;
            --grab-red: #d32f2f;
            --text-gray: #b0b0b0;
            --neon-red: #ff4d4d;
        }

        body {
            background-color: var(--bg-black);
            color: white;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            line-height: 1.6;
        }

        /* Navigation */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            background: rgba(0,0,0,0.9);
            position: fixed;
            width: 90%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #333;
        }

        nav a { color: white; text-decoration: none; margin-left: 20px; font-weight: bold; font-size: 0.9rem; }
        nav a:hover { color: var(--neon-red); }

        /* Hero Section */
        header {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070'); /* Cyber background */
            background-size: cover;
        }

        header h1 { font-size: 4rem; margin: 0; letter-spacing: 5px; color: var(--neon-red); }
        header p { font-size: 1.2rem; color: var(--text-gray); max-width: 600px; }

        /* Sections */
        section { padding: 80px 10%; }
        h2 { border-left: 5px solid var(--grab-red); padding-left: 15px; text-transform: uppercase; letter-spacing: 2px; }

        /* Project Card */
        .project-card {
            background: var(--card-bg);
            border: 1px solid #222;
            padding: 30px;
            border-radius: 8px;
            transition: 0.3s;
        }

        .project-card:hover { border-color: var(--neon-red); box-shadow: 0 0 20px rgba(255, 77, 77, 0.2); }

        .tag {
            background: var(--grab-red);
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-right: 5px;
        }

        /* Skills Grid */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .skill-item { background: #1a1a1a; padding: 20px; border-radius: 5px; text-align: center; }

        .btn {
            display: inline-block;
            background: var(--grab-red);
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <nav>
        <div style="font-size: 1.5rem; color: var(--neon-red);">YUMI.SEC</div>
        <div>
            <a href="#projects">PROJECTS</a>
            <a href="#experience">EXPERIENCE</a>
            <a href="#skills">SKILLS</a>
        </div>
    </nav>

    <header>
        <h1>NAKAOKA YUMI</h1>
        <p>Cybersecurity & Digital Forensics | Specialized in Secure IAM & Incident Response</p>
        <a href="#projects" class="btn">VIEW PROJECTS</a>
    </header>

    <section id="projects">
        <h2>Featured Project</h2>
        <div class="project-card">
            <h3>Secure Identity & Access Management (IAM) Portal</h3>
            <p>Developed a secure authentication gateway designed to mitigate **OWASP Top 10** vulnerabilities. Features include **PBKDF2 SHA-256** hashing and automated audit logging for **PDPA** compliance.</p>
            <div style="margin-bottom: 20px;">
                <span class="tag">Python</span>
                <span class="tag">Flask</span>
                <span class="tag">SQLite</span>
                <span class="tag">Git</span>
            </div>
            <a href="https://github.com/nakaokayumi/secure-identity-portal" class="btn" style="background: transparent; border: 1px solid var(--neon-red);">View Code on GitHub</a>
        </div>
    </section>

    <section id="experience" style="background: #0f0f0f;">
        <h2>Experience & Training</h2>
        <div class="grid">
            <div class="skill-item">
                <h4 style="color: var(--neon-red);">DIS Sentinel Programme</h4>
                <p>3rd Place in Red Team Hackathon. Focused on incident response and operational discipline.</p>
            </div>
            <div class="skill-item">
                <h4 style="color: var(--neon-red);">Kimberly Clark AP</h4>
                <p>Managed sensitive evidence and sample integrity with strict adherence to SOPs and audit standards.</p>
            </div>
        </div>
    </section>

    <section id="skills">
        <h2>Technical Core</h2>
        <div class="grid">
            <div class="skill-item"><strong>Networking</strong><br>TCP/IP, DNS, HTTP/S, APIs</div>
            <div class="skill-item"><strong>Systems</strong><br>Linux (CLI), Windows Event Viewer</div>
            <div class="skill-item"><strong>Security</strong><br>CompTIA Security+, Vulnerability Scanning</div>
            <div class="skill-item"><strong>Cloud</strong><br>AWS/GCP Fundamentals</div>
        </div>
    </section>

    <footer style="text-align: center; padding: 40px; color: var(--text-gray); border-top: 1px solid #222;">
        <p>nakaoka.yumi.sg@gmail.com | +65 8750 9811</p>
        <p>&copy; 2026 Nakaoka Yumi. All Rights Reserved.</p>
    </footer>

</body>
</html>
