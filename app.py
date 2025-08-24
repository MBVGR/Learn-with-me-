import streamlit as st

# --- Page Configuration and Styling ---
st.set_page_config(layout="wide")

# Custom CSS for the dark theme.
st.markdown("""
<style>
    .stApp {
        background-color: #282a36; /* Dark background */
        color: #f8f8f2; /* Light text color */
    }
    h1, h2, h3, h4 {
        color: #8be9fd; /* Cyan for headings */
    }
    .hero-section {
        background-color: #44475a;
        color: white;
        padding: 100px 20px;
        text-align: center;
        border-radius: 0 0 20px 20px;
    }
    .hero-section h1 {
        color: #50fa7b; /* Green accent for hero title */
        font-size: 3em;
        margin-bottom: 0.2em;
    }
    .hero-section p {
        font-size: 1.2em;
    }
    .button {
        background-color: #ff79c6;
        color: #f8f8f2;
        padding: 12px 25px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 600;
    }
    .button:hover {
        background-color: #bd688f;
    }
    .sidebar-section {
        background-color: #44475a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    .sidebar-section h4 {
        color: #ffb86c; /* Orange for sidebar headings */
    }
    .course-card {
        background-color: #44475a;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
        color: #f8f8f2;
    }
    .course-card:hover {
        transform: translateY(-5px);
        background-color: #6272a4;
    }
    .course-card h3 {
        color: #f1fa8c; /* Yellow for course titles */
    }
    .course-card .price {
        font-size: 1.5em;
        font-weight: 600;
        color: #ff79c6; /* Pink for prices */
    }
</style>
""", unsafe_allow_html=True)


# --- Hero Section ---
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1>Learn Python with Me</h1>
        <p>Unlock your potential with expert-led Python programming courses.</p>
        <a href="#courses-section" class="button">Explore Courses</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content and sidebar container
col_main, col_sidebar = st.columns([3, 1])

with col_main:
    st.markdown("<h2 id='courses-section'>My Python Courses</h2>", unsafe_allow_html=True)
    
    course_col1, course_col2, course_col3 = st.columns(3)

    with course_col1:
        st.markdown("""
        <div class="course-card">
            <h3>Python Fundamentals</h3>
            <p>A beginner-friendly course to get you started with the basics of Python programming.</p>
            <span class="price">$99</span>
        </div>
        """, unsafe_allow_html=True)
    
    with course_col2:
        st.markdown("""
        <div class="course-card">
            <h3>Web Development with Django</h3>
            <p>Learn to build robust web applications using the powerful Django framework.</p>
            <span class="price">$149</span>
        </div>
        """, unsafe_allow_html=True)

    with course_col3:
        st.markdown("""
        <div class="course-card">
            <h3>Data Science with Python</h3>
            <p>Dive into data analysis, visualization, and machine learning with Python libraries.</p>
            <span class="price">$199</span>
        </div>
        """, unsafe_allow_html=True)


with col_sidebar:
    st.markdown("""
    <div class="sidebar-section registration-form">
        <h4>Enroll Now</h4>
        <p>Fill out the form below to register your interest for any course.</p>
        <iframe src="YOUR_GOOGLE_FORM_EMBED_URL_HERE" width="100%" height="300" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-section contact-info">
        <h4>Contact Me</h4>
        <p>Have a question? Feel free to reach out for help!</p>
        <ul>
            <li><strong>Email:</strong> your.email@example.com</li>
            <li><strong>LinkedIn:</strong> <a href="YOUR_LINKEDIN_URL_HERE" target="_blank">Your Name</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #f8f8f2;">
    &copy; 2025 [Your Name]. All rights reserved.
</div>
""", unsafe_allow_html=True)