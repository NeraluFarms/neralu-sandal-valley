import re

with open('campaign.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''        /* ========================================================
           NERALU ELITE CAMPAIGN ENGINE - AESTHETIC OVERHAUL
           ======================================================== */
        :root {
            --primary-teal: #033E3E;
            --accent-gold: #F0E0C6;
            --bg-cream: #FFF9E9;
            --bg-almond: #F4E6D2;
            --dark-charcoal: #0a1a16;
            --white: #FFFFFF;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--bg-cream) !important;
            color: var(--primary-teal);
            line-height: 1.6;
            overflow-x: hidden;
        }
        .serif { font-family: 'Playfair Display', serif; }

        /* --- 1. Trust Strip Top Bar --- */
        .trust-strip {
            background-color: var(--dark-charcoal);
            color: var(--white);
            padding: 10px 20px;
            text-align: center;
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 600;
            position: relative;
            z-index: 1005;
        }

        /* --- 2. Translucent Floating Navbar --- */
        header {
            position: absolute;
            top: 65px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 1300px;
            background: rgba(3, 62, 62, 0.9) !important;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(240, 224, 198, 0.2) !important;
            border-radius: 50px;
            padding: 12px 40px;
            z-index: 1000;
            box-shadow: 0 15px 35px rgba(3, 62, 62, 0.15) !important;
        }

        .nav-inner { display: flex; justify-content: space-between; align-items: center; }
        .logo img { max-height: 40px; filter: brightness(0) invert(1); }

        .hamburger {
            cursor: pointer;
            display: flex !important;
            flex-direction: column !important;
            gap: 5px !important;
            width: 40px;
            height: 40px;
            justify-content: center;
            align-items: center;
        }
        .hamburger span {
            display: block;
            background-color: var(--accent-gold) !important;
            width: 26px;
            height: 3px;
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        /* --- 3. Overlay System Navigation --- */
        .menu-overlay {
            position: fixed;
            inset: 0;
            background-color: var(--dark-charcoal) !important;
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.4s ease;
        }
        .menu-overlay.active { opacity: 1; visibility: visible; }
        .close-menu {
            position: absolute;
            top: 40px;
            right: 5%;
            font-size: 2.5rem;
            color: var(--accent-gold) !important;
            cursor: pointer;
        }
        .menu-links { list-style: none; text-align: center; }
        .menu-links li { margin: 25px 0; }
        .menu-links a {
            color: var(--accent-gold) !important;
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .menu-links a:hover, .close-menu:hover { color: var(--bg-cream) !important; }

        /* --- 4. Immersive Cinematic Hero --- */
        .campaign-hero {
            position: relative;
            width: 100%;
            height: 95vh;
            min-height: 700px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding: 0 8%;
            overflow: hidden;
        }

        .hero-media-panel {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        .hero-video-bg {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .dark-vignette {
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 20% 30%, rgba(10, 26, 22, 0.2) 0%, rgba(10, 26, 22, 0.85) 100%);
            z-index: 2;
        }

        /* Floating Glass Form Card */
        .campaign-card-form {
            position: relative;
            z-index: 10;
            background: rgba(255, 255, 255, 0.85) !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            padding: 50px 40px;
            border-radius: 24px;
            box-shadow: 0 30px 60px rgba(10, 26, 22, 0.25);
            width: 100%;
            max-width: 460px;
        }

        .campaign-card-form h3 {
            font-family: 'Playfair Display', serif;
            color: var(--primary-teal);
            font-size: 2.2rem;
            line-height: 1.2;
            margin-bottom: 12px;
            text-align: center;
        }

        .campaign-card-form p {
            font-size: 0.9rem;
            color: #666;
            text-align: center;
            margin-bottom: 25px;
            line-height: 1.4;
        }

        .form-bubble-group {
            margin-bottom: 20px;
            position: relative;
        }

        .form-bubble-group i {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--primary-teal);
            opacity: 0.7;
            z-index: 1;
        }

        .form-bubble-group input, 
        .form-bubble-group select {
            width: 100%;
            background-color: rgba(3, 62, 62, 0.04) !important;
            border: 1px solid rgba(3, 62, 62, 0.08) !important;
            border-radius: 12px !important;
            padding: 16px 16px 16px 48px !important;
            color: var(--primary-teal);
            font-family: 'Montserrat', sans-serif;
            font-size: 0.95rem;
            outline: none;
            transition: all 0.3s ease;
        }

        .form-bubble-group input:focus,
        .form-bubble-group select:focus {
            border-color: var(--primary-teal) !important;
            background-color: var(--white) !important;
            box-shadow: 0 4px 12px rgba(3, 62, 62, 0.1);
        }

        .btn-campaign-submit {
            width: 100%;
            background-color: var(--primary-teal) !important;
            color: var(--bg-cream) !important;
            border: none;
            padding: 18px !important;
            font-size: 1rem;
            border-radius: 12px !important;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(3, 62, 62, 0.25) !important;
            transition: all 0.3s ease;
        }

        .btn-campaign-submit:hover {
            background-color: var(--dark-charcoal) !important;
            transform: translateY(-2px);
            color: var(--white) !important;
        }

        /* --- 5. Premium Overlapping Matrix Cards --- */
        .matrix-section {
            padding: 120px 0;
            background-color: var(--bg-almond) !important;
            position: relative;
            text-align: center;
        }

        .matrix-section h2 {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            color: var(--primary-teal);
            letter-spacing: -1px;
            margin-bottom: 15px;
        }

        .matrix-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 60px auto 0;
            padding: 0 20px;
        }

        .matrix-card {
            background: var(--bg-cream) !important;
            border-radius: 24px !important;
            border-top: none !important;
            border-left: 6px solid var(--primary-teal) !important;
            padding: 40px !important;
            box-shadow: 0 20px 45px rgba(3, 62, 62, 0.06) !important;
            text-align: left;
            transition: transform 0.3s ease;
        }

        .matrix-card:hover { transform: translateY(-5px); }

        .matrix-tag {
            display: inline-block;
            font-size: 11px;
            background-color: var(--primary-teal) !important;
            color: var(--bg-cream) !important;
            padding: 6px 16px;
            border-radius: 50px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 15px;
            letter-spacing: 1px;
        }

        .matrix-card h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            color: var(--dark-charcoal);
            margin-bottom: 20px;
        }

        .matrix-specs-list {
            list-style: none;
            padding: 0;
            margin-bottom: 30px;
        }

        .matrix-specs-list li {
            font-size: 0.95rem;
            padding: 12px 0;
            border-bottom: 1px solid var(--bg-almond);
            display: flex;
            justify-content: space-between;
            color: #555;
        }

        .matrix-specs-list li strong { color: var(--primary-teal); }

        .btn-matrix-action {
            display: block;
            width: 100%;
            text-align: center;
            background: transparent;
            border-radius: 30px !important;
            border: 2px solid var(--primary-teal) !important;
            color: var(--primary-teal) !important;
            padding: 14px !important;
            text-decoration: none;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 1px;
            transition: all 0.3s ease;
        }

        .matrix-card:hover .btn-matrix-action {
            background: var(--primary-teal) !important;
            color: var(--bg-cream) !important;
        }

        /* --- 6. Luxury Accordions --- */
        .faq-section {
            padding: 100px 0;
            background-color: var(--bg-cream);
        }

        .faq-container { max-width: 800px; margin: 0 auto; padding: 0 20px; }
        .faq-header { text-align: center; margin-bottom: 40px; }
        .faq-title { color: var(--primary-teal); font-size: 2.5rem; }

        .faq-item {
            border-radius: 16px !important;
            margin-bottom: 20px;
            border: 1px solid rgba(3, 62, 62, 0.08) !important;
            background: var(--white);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }

        .faq-question {
            width: 100%;
            text-align: left;
            padding: 24px 30px !important;
            background: transparent;
            border: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--dark-charcoal);
            cursor: pointer;
            font-family: 'Montserrat', sans-serif;
            transition: all 0.3s ease;
        }

        .faq-question i { color: var(--primary-teal); transition: transform 0.3s ease; }
        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            background: var(--bg-almond);
        }
        .faq-answer p { padding: 0 30px 20px; color: #555; font-size: 0.95rem; line-height: 1.6; }
        .faq-item.active .faq-question { color: var(--primary-teal); }
        .faq-item.active .faq-question i { transform: rotate(45deg); }
        .faq-item.active .faq-answer { max-height: 500px; }

        /* --- 7. Footer --- */
        footer {
            background-color: var(--dark-charcoal);
            color: var(--white);
            padding: 80px 0 30px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .footer-title {
            color: var(--accent-gold);
            font-size: 1.2rem;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .footer-col p { color: #ccc; font-size: 0.95rem; line-height: 1.6; margin-bottom: 10px; }
        .footer-links { list-style: none; }
        .footer-links li { margin-bottom: 12px; }
        .footer-links a { color: #ccc; text-decoration: none; transition: color 0.3s ease; font-size: 0.95rem; }
        .footer-links a:hover { color: var(--white); }
        .social-icons { display: flex; gap: 15px; }
        .social-icon {
            display: inline-flex; justify-content: center; align-items: center;
            width: 40px; height: 40px; background: rgba(255, 255, 255, 0.1);
            border-radius: 50%; color: var(--white); text-decoration: none;
            transition: all 0.3s ease;
        }
        .social-icon:hover { background: var(--accent-gold); transform: translateY(-3px); color: var(--dark-charcoal); }

        .footer-bottom {
            max-width: 1200px; margin: 50px auto 0; padding: 20px 20px 0;
            border-top: 1px solid rgba(240, 224, 198, 0.1); display: flex;
            justify-content: space-between; align-items: center; flex-wrap: wrap;
            gap: 20px; color: #999; font-size: 0.85rem;
        }
        .legal-links a { color: #999; text-decoration: none; margin: 0 10px; transition: color 0.3s ease; }
        .legal-links a:hover { color: var(--white); }

        /* --- 8. Floating Buttons --- */
        .floating-buttons { position: fixed; bottom: 30px; right: 30px; display: flex; flex-direction: column; gap: 15px; z-index: 1000; }
        .float-btn {
            width: 60px; height: 60px; border-radius: 50%; display: flex;
            justify-content: center; align-items: center; font-size: 28px;
            color: white; text-decoration: none; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }
        .float-btn:hover { transform: scale(1.1); }
        .call-btn { background-color: var(--primary-teal); }
        .whatsapp-btn { background-color: #25D366; }

        /* Mobile Fallbacks */
        @media (max-width: 991px) {
            .campaign-hero { justify-content: center; padding: 140px 20px 60px; height: auto; }
            .campaign-card-form { background: var(--bg-cream) !important; }
        }'''

content = re.sub(r'<style>.*?</style>', '<style>\n' + new_css + '\n    </style>', content, flags=re.DOTALL)
content = content.replace('<!-- Right Conversion Panel -->\n        <div class="hero-conversion-panel">\n            <!-- Form Card -->', '<!-- Right Conversion Panel / Form Card -->')
content = content.replace('</form>\n            </div>\n        </div>', '</form>\n            </div>')

with open('campaign.html', 'w', encoding='utf-8') as f:
    f.write(content)
