import flet as ft
import os
import socket
from urllib.parse import quote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PORT = 8550

def available_port(preferred_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("0.0.0.0", preferred_port))
            return preferred_port
        except OSError:
            sock.bind(("0.0.0.0", 0))
            return sock.getsockname()[1]

def asset_src(filename):
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        return filename

    wanted = filename.replace(" ", "").lower()
    wanted_stem, wanted_ext = os.path.splitext(wanted)

    for actual in os.listdir(BASE_DIR):
        actual_clean = actual.replace(" ", "").lower()
        actual_stem, _ = os.path.splitext(actual_clean)
        if actual_clean == wanted or actual_stem == wanted_stem:
            return actual
        if actual_stem.startswith(wanted_stem) and wanted_ext in actual_clean:
            return actual

    return filename

def asset_url(filename):
    return f"/{quote(asset_src(filename), safe='/')}"

def main(page: ft.Page):
    page.title = "Tomas Shiyanga | Portfolio"
    page.bgcolor = "#0A0A1A"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    def build_nav():
        return ft.Container(
            content=ft.Row([
                ft.Text("TS", size=20, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                ft.Row([
                    ft.TextButton("Home", on_click=show_home, style=ft.ButtonStyle(color="#00FFFF")),
                    ft.TextButton("Timeline", on_click=show_timeline, style=ft.ButtonStyle(color="#00FFFF")),
                    ft.TextButton("MATLAB", on_click=show_matlab, style=ft.ButtonStyle(color="#00FFFF")),
                    ft.TextButton("Blog", on_click=show_blog, style=ft.ButtonStyle(color="#00FFFF")),
                    ft.TextButton("GitHub", on_click=show_github, style=ft.ButtonStyle(color="#00FFFF")),
                ]),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor="#111133",
            padding=ft.padding.symmetric(horizontal=30, vertical=15),
            border=ft.border.only(bottom=ft.BorderSide(2, "#00FFFF")),
        )

    def img(filename):
        return ft.Container(
            content=ft.Image(src=asset_url(filename), width=600),
            border_radius=10,
            border=ft.border.all(1, "#00FFFF"),
            padding=5,
            margin=ft.margin.only(top=10, bottom=10),
        )

    def presentation_video_link():
        return ft.Container(
            content=ft.TextButton(
                "Watch Portfolio Presentation",
                url=asset_url("presentation.mp4"),
                style=ft.ButtonStyle(color="#00FFFF"),
            ),
            width=620,
            border_radius=10,
            border=ft.border.all(1, "#00FFFF"),
            padding=10,
            margin=ft.margin.only(top=10, bottom=10),
        )

    def section_title(text):
        return ft.Container(
            content=ft.Text(text, size=28, weight=ft.FontWeight.BOLD, color="#00FFFF"),
            margin=ft.margin.only(top=20, bottom=10),
        )

    def week_card(title, description):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                ft.Text(description, size=14, color="#CCCCCC"),
            ]),
            bgcolor="#111133",
            border_radius=12,
            border=ft.border.only(left=ft.BorderSide(4, "#00FFFF")),
            padding=20,
            margin=ft.margin.only(top=8, bottom=8),
        )

    def show_home(e=None):
        page.clean()
        page.add(
            build_nav(),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Image(src=asset_url("profile.jpg"), width=120, height=120),
                            border_radius=60,
                            border=ft.border.all(3, "#00FFFF"),
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        ),
                        ft.Column([
                            ft.Text("Tomas Shiyanga", size=42, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                            ft.Text("Python Developer | Computer Programming I", size=18, color="#FFFFFF"),
                            ft.Text("Semester 1, 2026  |  UNAM", size=14, color="#888888"),
                            ft.Text("GitHub: shiyangatomas", size=14, color="#00FFFF"),
                        ], spacing=5),
                    ], spacing=30),
                    ft.Divider(color="#223366", height=30),
                    ft.Text("About Me", size=26, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                    ft.Text("I am a Computer Programming I student at UNAM working on CorroCheck, a corrosion inspection app built for Metallurgical, Mining and Civil Engineering modules. I contributed by designing and coding the Home and History screens.", size=16, color="#CCCCCC"),
                    ft.Divider(color="#223366", height=30),
                    ft.Text("Portfolio Presentation", size=26, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                    presentation_video_link(),
                    ft.Divider(color="#223366", height=30),
                    ft.Text("My Contributions", size=26, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                    ft.Row([
                        ft.Container(
                            content=ft.Column([
                                ft.Text("🎨", size=30),
                                ft.Text("UI Design", size=16, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                                ft.Text("Home & History Screens in Figma", size=12, color="#AAAAAA"),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor="#111133",
                            border_radius=12,
                            border=ft.border.all(1, "#00FFFF"),
                            padding=20,
                            width=180,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("💻", size=30),
                                ft.Text("Coding", size=16, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                                ft.Text("HomeScreen.js in React Native", size=12, color="#AAAAAA"),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor="#111133",
                            border_radius=12,
                            border=ft.border.all(1, "#00FFFF"),
                            padding=20,
                            width=180,
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("🎓", size=30),
                                ft.Text("MATLAB", size=16, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                                ft.Text("7 Courses Completed", size=12, color="#AAAAAA"),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            bgcolor="#111133",
                            border_radius=12,
                            border=ft.border.all(1, "#00FFFF"),
                            padding=20,
                            width=180,
                        ),
                    ], spacing=20),
                ], spacing=15),
                padding=40,
            ),
        )
        page.update()

    def show_timeline(e=None):
        page.clean()
        page.add(
            build_nav(),
            ft.Container(
                content=ft.Column([
                    section_title("📅 Project Timeline"),
                    ft.Text("CorroCheck — UNAM Group 7", size=16, color="#888888"),
                    ft.Divider(color="#223366"),
                    week_card("Week 1 — Home Screen Design", "Designed the full CorroCheck home screen in Figma including the stats dashboard, New Inspection button, Recent Activity section and Shortcuts panel."),
                    img("home_final.jpg"),
                    week_card("Week 2 — History Screen Design", "Designed the History screen showing all past inspections with search functionality, inspection details, corrosion type and severity levels."),
                    img("history_screen.jpg"),
                    week_card("Week 3 — Coded HomeScreen.js", "Implemented the home screen in React Native including bottom navigation, shortcuts panel, upload button and search functionality."),
                    img("github2.jpg"),
                    ft.Divider(color="#223366"),
                    ft.Text("Design Process Screenshots", size=20, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                    img("corrocheck1.jpg"),
                    img("corrocheck2.jpg"),
                    img("corrocheck3.jpg"),
                    img("corrocheck4.jpg"),
                    img("corrocheck5.jpg"),
                    img("corrocheck6.jpg"),
                    img("corrocheck7.jpg"),
                ]),
                padding=40,
            ),
        )
        page.update()

    def show_matlab(e=None):
        page.clean()
        page.add(
            build_nav(),
            ft.Container(
                content=ft.Column([
                    section_title("🎓 MATLAB Achievement Hub"),
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text("7", size=48, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                                ft.Text("Completed", size=14, color="#AAAAAA"),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Column([
                                ft.Text("7", size=48, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                                ft.Text("Total", size=14, color="#AAAAAA"),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ], spacing=40),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#223366"),
                        padding=20,
                        margin=ft.margin.only(bottom=20),
                    ),
                    ft.Divider(color="#223366"),
                    ft.Text("MATLAB Onramp — 30 March 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert1.jpg"),
                    ft.Text("Simulink Onramp — 12 April 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert2.jpg"),
                    ft.Text("Calculations with Vectors and Matrices — 31 March 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert3.jpg"),
                    ft.Text("Explore Data with MATLAB Plots — 18 April 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert4.jpg"),
                    ft.Text("Make and Manipulate Matrices — 17 April 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert5.jpg"),
                    ft.Text("Machine Learning Onramp — 23 April 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert6.jpg"),
                    ft.Text("Simulink Fundamentals — 27 April 2026", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    img("cert7.jpg"),
                ]),
                padding=40,
            ),
        )
        page.update()

    def show_blog(e=None):
        page.clean()
        page.add(
            build_nav(),
            ft.Container(
                content=ft.Column([
                    section_title("📝 Technical Blog"),
                    ft.Text("Confidence in Concepts", size=18, color="#888888"),
                    ft.Divider(color="#223366"),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Variables in Python", size=20, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                            ft.Text("A variable is a container that stores data. In Python you do not need to declare the type — just assign a value and Python figures it out.", size=14, color="#CCCCCC"),
                            ft.Container(
                                content=ft.Text("name = 'Tomas'  |  age = 20  |  gpa = 3.5", size=13, color="#00FF88"),
                                bgcolor="#0A1628",
                                border_radius=8,
                                padding=15,
                                margin=ft.margin.only(top=10),
                            ),
                        ]),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#223366"),
                        padding=25,
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Functions in Python", size=20, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                            ft.Text("A function is a block of reusable code. You define it once and call it many times.", size=14, color="#CCCCCC"),
                            ft.Container(
                                content=ft.Text("def greet():\n    print('Hello Tomas')", size=13, color="#00FF88"),
                                bgcolor="#0A1628",
                                border_radius=8,
                                padding=15,
                                margin=ft.margin.only(top=10),
                            ),
                        ]),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#223366"),
                        padding=25,
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Introduction to Flet", size=20, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                            ft.Text("Flet is a Python framework that lets you build web, desktop and mobile apps using only Python. No HTML or CSS needed!", size=14, color="#CCCCCC"),
                            ft.Container(
                                content=ft.Text("import flet as ft\nft.run(main)", size=13, color="#00FF88"),
                                bgcolor="#0A1628",
                                border_radius=8,
                                padding=15,
                                margin=ft.margin.only(top=10),
                            ),
                            ft.Text("This entire portfolio was built using Flet!", size=13, color="#00FFFF"),
                        ]),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#223366"),
                        padding=25,
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                ]),
                padding=40,
            ),
        )
        page.update()

    def show_github(e=None):
        page.clean()
        page.add(
            build_nav(),
            ft.Container(
                content=ft.Column([
                    section_title("🐙 GitHub Evidence"),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("GitHub Username: shiyangatomas", size=16, color="#FFFFFF"),
                            ft.Text("Repository: UNAM-I3691CP-Group7-CorroCheck", size=16, color="#00FFFF"),
                        ]),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#223366"),
                        padding=20,
                        margin=ft.margin.only(bottom=20),
                    ),
                    ft.Divider(color="#223366"),
                    week_card("Contribution 1 — Home Screen Design", "Designed the full CorroCheck home screen including stats dashboard, New Inspection button, Recent Activity section and Shortcuts panel."),
                    img("home_final.jpg"),
                    week_card("Contribution 2 — History Screen Design", "Designed the History screen with search functionality, inspection list, corrosion types and severity indicators."),
                    img("history_screen.jpg"),
                    week_card("Contribution 3 — HomeScreen.js Code", "Coded the HomeScreen.js in React Native implementing bottom navigation, shortcuts, upload button and search functionality."),
                    img("github2.jpg"),
                    week_card("Repository Structure", "Full project structure showing all components, screens, navigation and services."),
                    img("github1.jpg"),
                    ft.Divider(color="#223366"),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Impact Summary", size=18, weight=ft.FontWeight.BOLD, color="#00FFFF"),
                            ft.Text("My screen designs and code formed the foundation of the CorroCheck app UI which the rest of the 20 member team built their features on top of.", size=14, color="#CCCCCC"),
                        ]),
                        bgcolor="#111133",
                        border_radius=12,
                        border=ft.border.all(1, "#00FFFF"),
                        padding=20,
                        margin=ft.margin.only(top=8, bottom=8),
                    ),
                ]),
                padding=40,
            ),
        )
        page.update()

    show_home()

if __name__ == "__main__":
    if "PORT" in os.environ:
        PORT = int(os.environ["PORT"])
        view = None
    else:
        PORT = available_port(PORT)
        view = ft.AppView.WEB_BROWSER

    ft.run(main, view=view, port=PORT, assets_dir=BASE_DIR)
