from flask import Flask, render_template

app = Flask(__name__)

# Edit these details when you have your confirmed academic information.
PORTFOLIO = {
    "name": "Ramyasri",
    "headline": "Entrepreneur | Co-founder & Director",
    "tagline": "Building meaningful opportunities through technology, education, and innovation.",
    "intro": (
        "I am an entrepreneurial professional interested in technology, education, "
        "innovation, and creating practical learning opportunities."
    ),
    "email": "support@wayeva.com",  # Replace with your personal professional email
    "linkedin": "https://www.linkedin.com/company/wayeva/",  # Replace with your personal LinkedIn
    "github": "#",  # Add your GitHub profile
    "education": [
        {
            "qualification": "Add your degree / qualification",
            "institution": "Add your college or university",
            "year": "Add graduation year",
            "note": "Update this section with your confirmed academic details."
        }
    ],
    "skills": [
        "Leadership & Team Coordination",
        "Business Development",
        "Communication",
        "Project Coordination",
        "Operations & Planning",
        "Student Skill Development"
    ],
    "projects": [
        {
            "title": "Student Skill Development Programs",
            "category": "Education & Program Development",
            "description": "Supported the planning and coordination of industry-relevant training and certification initiatives for students.",
            "tags": ["Program Design", "Student Development", "Coordination"],
            "link": "#"
        },
        {
            "title": "College Collaboration Initiatives",
            "category": "Partnerships & Business Development",
            "description": "Worked on institutional proposals, college partnerships, and collaboration processes through Wayeva Innovations.",
            "tags": ["Partnerships", "Business Development", "Communication"],
            "link": "#"
        },
        {
            "title": "Career Development & Internship Operations",
            "category": "Career Readiness",
            "description": "Contributed to internship program operations, project-based learning coordination, and student career support.",
            "tags": ["Internships", "Career Development", "Operations"],
            "link": "#"
        }
    ],
    "experience": [
        {
            "role": "Co-founder & Director",
            "company": "Wayeva Innovations Private Limited",
            "period": "Add your start date – Present",
            "description": "Involved in business operations, college partnerships, student training initiatives, team coordination, and company planning."
        }
    ],
    "certifications": [
        "Add your completed certifications here"
    ],
    "achievements": [
        "Co-building an education and skill-development company",
        "Contributing to college collaboration and student development initiatives"
    ],
    "interests": [
        "Entrepreneurship",
        "Technology & Innovation",
        "Education",
        "Leadership",
        "Personal Growth"
    ]
}

@app.route("/")
def home():
    return render_template("index.html", portfolio=PORTFOLIO)

if __name__ == "__main__":
    app.run(debug=True)
