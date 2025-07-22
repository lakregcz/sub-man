import flet as ft
import mysql.connector
from datetime import datetime
import asyncio


class SubscriptionApp:
    def __init__(self):
        self.current_user = None
        self.page = None
        self.db = None
        self.setup_database()

    def setup_database(self):
        try:
            self.db = mysql.connector.connect(
                host='XXX',
                database='XXX',
                user='XXX',
                password='XXX'
            )
        except Exception as e:
            print(f"Database connection failed: {e}")

    def main(self, page: ft.Page):
        self.page = page

        # Page configuration
        page.title = "Premium Subscription Manager"
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = "#0a0a0a"
        page.window.width = 500
        page.window.height = 700
        page.window.resizable = False
        page.window.center()

        # Custom theme
        page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#6366f1",
                primary_container="#4f46e5",
                secondary="#8b5cf6",
                background="#0a0a0a",
                surface="#111111",
                surface_variant="#1f1f1f"
            )
        )

        self.show_login()

    def clear_page(self):
        self.page.controls.clear()

    def show_login(self):
        self.clear_page()
        self.current_user = None

        # Main container with gradient background
        main_container = ft.Container(
            content=ft.Column([
                # Header section
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Icon(
                                ft.Icons.LOCK_ROUNDED,
                                size=32,
                                color="#6366f1"
                            ),
                            bgcolor="#6366f1",
                            width=60,
                            height=60,
                            border_radius=30,
                            alignment=ft.alignment.center,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.Colors.with_opacity(0.3, "#6366f1")
                            )
                        ),
                        ft.Column([
                            ft.Text(
                                "Premium Manager",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            ),
                            ft.Text(
                                "Welcome back",
                                size=14,
                                color="#9ca3af"
                            )
                        ], spacing=2, expand=True)
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                    padding=ft.padding.all(30),
                    margin=ft.margin.only(bottom=30)
                ),

                # Login form
                ft.Container(
                    content=ft.Column([
                        # Username field
                        ft.Column([
                            ft.Text(
                                "Username",
                                size=14,
                                weight=ft.FontWeight.W_500,
                                color="#d1d5db"
                            ),
                            ft.TextField(
                                ref=ft.Ref[ft.TextField](),
                                hint_text="Enter your username",
                                bgcolor="#1f1f1f",
                                border_color="#374151",
                                focused_border_color="#6366f1",
                                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                                hint_style=ft.TextStyle(color="#6b7280"),
                                content_padding=ft.padding.all(15),
                                border_radius=12,
                                prefix_icon=ft.Icons.PERSON_OUTLINE
                            )
                        ], spacing=8),

                        # Password field
                        ft.Column([
                            ft.Text(
                                "Password",
                                size=14,
                                weight=ft.FontWeight.W_500,
                                color="#d1d5db"
                            ),
                            ft.TextField(
                                ref=ft.Ref[ft.TextField](),
                                hint_text="Enter your password",
                                password=True,
                                can_reveal_password=True,
                                bgcolor="#1f1f1f",
                                border_color="#374151",
                                focused_border_color="#6366f1",
                                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                                hint_style=ft.TextStyle(color="#6b7280"),
                                content_padding=ft.padding.all(15),
                                border_radius=12,
                                prefix_icon=ft.Icons.LOCK_OUTLINE
                            )
                        ], spacing=8),

                        # Login button
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="Sign In",
                                on_click=self.login,
                                style=ft.ButtonStyle(
                                    bgcolor="#6366f1",
                                    color=ft.Colors.WHITE,
                                    elevation=0,
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    padding=ft.padding.symmetric(vertical=15)
                                ),
                                width=float('inf')
                            ),
                            margin=ft.margin.only(top=10)
                        ),

                        # Divider - Fixed by removing expand parameter and using Container
                        ft.Container(
                            content=ft.Row([
                                ft.Container(
                                    content=ft.Divider(height=1, color="#374151"),
                                    expand=True
                                ),
                                ft.Container(
                                    content=ft.Text("or", size=12, color="#6b7280"),
                                    padding=ft.padding.symmetric(horizontal=15)
                                ),
                                ft.Container(
                                    content=ft.Divider(height=1, color="#374151"),
                                    expand=True
                                )
                            ]),
                            margin=ft.margin.symmetric(vertical=20)
                        ),

                        # Register button
                        ft.OutlinedButton(
                            text="Create New Account",
                            on_click=lambda _: self.show_register(),
                            style=ft.ButtonStyle(
                                color="#6366f1",
                                side=ft.BorderSide(color="#6366f1", width=1),
                                shape=ft.RoundedRectangleBorder(radius=12),
                                padding=ft.padding.symmetric(vertical=15)
                            ),
                            width=float('inf')
                        )
                    ], spacing=20),
                    bgcolor="#111111",
                    padding=ft.padding.all(30),
                    border_radius=20,
                    border=ft.border.all(1, "#1f1f1f"),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=20,
                        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                    )
                ),

                # Support info
                ft.Container(
                    content=ft.Text(
                        "Contact support: contact@lakiup.com",
                        size=12,
                        color="#6b7280",
                        text_align=ft.TextAlign.CENTER
                    ),
                    margin=ft.margin.only(top=30)
                )
            ], spacing=0, scroll=ft.ScrollMode.AUTO),
            padding=ft.padding.all(30),
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#0a0a0a", "#111111"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            )
        )

        # Store references for form fields
        self.username_field = main_container.content.controls[1].content.controls[0].controls[1]
        self.password_field = main_container.content.controls[1].content.controls[1].controls[1]

        self.page.add(main_container)
        self.page.update()

    def show_register(self):
        self.clear_page()

        main_container = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color="#6b7280",
                            on_click=lambda _: self.show_login()
                        ),
                        ft.Column([
                            ft.Text(
                                "Create Account",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            ),
                            ft.Text(
                                "Join thousands of satisfied users",
                                size=14,
                                color="#9ca3af"
                            )
                        ], expand=True, spacing=2)
                    ]),
                    padding=ft.padding.all(20),
                    margin=ft.margin.only(bottom=20)
                ),

                # Register form
                ft.Container(
                    content=ft.Column([
                        # Username field
                        ft.Column([
                            ft.Text("Username", size=14, weight=ft.FontWeight.W_500, color="#d1d5db"),
                            ft.TextField(
                                ref=ft.Ref[ft.TextField](),
                                hint_text="Choose a username",
                                bgcolor="#1f1f1f",
                                border_color="#374151",
                                focused_border_color="#6366f1",
                                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                                hint_style=ft.TextStyle(color="#6b7280"),
                                content_padding=ft.padding.all(15),
                                border_radius=12,
                                prefix_icon=ft.Icons.PERSON_OUTLINE
                            )
                        ], spacing=8),

                        # Email field
                        ft.Column([
                            ft.Text("Email", size=14, weight=ft.FontWeight.W_500, color="#d1d5db"),
                            ft.TextField(
                                ref=ft.Ref[ft.TextField](),
                                hint_text="Enter your email",
                                bgcolor="#1f1f1f",
                                border_color="#374151",
                                focused_border_color="#6366f1",
                                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                                hint_style=ft.TextStyle(color="#6b7280"),
                                content_padding=ft.padding.all(15),
                                border_radius=12,
                                prefix_icon=ft.Icons.EMAIL_OUTLINED
                            )
                        ], spacing=8),

                        # Password field
                        ft.Column([
                            ft.Text("Password", size=14, weight=ft.FontWeight.W_500, color="#d1d5db"),
                            ft.TextField(
                                ref=ft.Ref[ft.TextField](),
                                hint_text="Create a password",
                                password=True,
                                can_reveal_password=True,
                                bgcolor="#1f1f1f",
                                border_color="#374151",
                                focused_border_color="#6366f1",
                                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                                hint_style=ft.TextStyle(color="#6b7280"),
                                content_padding=ft.padding.all(15),
                                border_radius=12,
                                prefix_icon=ft.Icons.LOCK_OUTLINE
                            )
                        ], spacing=8),

                        # Create account button
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="Create Account",
                                on_click=self.register,
                                style=ft.ButtonStyle(
                                    bgcolor="#10b981",
                                    color=ft.Colors.WHITE,
                                    elevation=0,
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    padding=ft.padding.symmetric(vertical=15)
                                ),
                                width=float('inf')
                            ),
                            margin=ft.margin.only(top=20)
                        )
                    ], spacing=20),
                    bgcolor="#111111",
                    padding=ft.padding.all(30),
                    border_radius=20,
                    border=ft.border.all(1, "#1f1f1f"),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=20,
                        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                    )
                ),

                # Support info
                ft.Container(
                    content=ft.Text(
                        "Contact support: contact@lakiup.com",
                        size=12,
                        color="#6b7280",
                        text_align=ft.TextAlign.CENTER
                    ),
                    margin=ft.margin.only(top=30)
                )
            ], scroll=ft.ScrollMode.AUTO),
            padding=ft.padding.all(30),
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#0a0a0a", "#111111"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            )
        )

        # Store field references
        self.reg_username_field = main_container.content.controls[1].content.controls[0].controls[1]
        self.reg_email_field = main_container.content.controls[1].content.controls[1].controls[1]
        self.reg_password_field = main_container.content.controls[1].content.controls[2].controls[1]

        self.page.add(main_container)
        self.page.update()

    def show_main_app(self):
        self.clear_page()

        # Check subscription status
        has_subscription = False
        subscription_end = None

        if self.db:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute(
                "SELECT subscription_end FROM users WHERE id = %s",
                (self.current_user['id'],)
            )
            result = cursor.fetchone()
            if result and result['subscription_end']:
                subscription_end = result['subscription_end']
                has_subscription = datetime.now() < subscription_end

        main_container = ft.Container(
            content=ft.Column([
                # Header with user info
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Text(
                                self.current_user['username'][0].upper(),
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            ),
                            bgcolor="#6366f1",
                            width=50,
                            height=50,
                            border_radius=25,
                            alignment=ft.alignment.center
                        ),
                        ft.Column([
                            ft.Text(
                                f"Welcome back, {self.current_user['username']}!",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            ),
                            ft.Text(
                                "Manage your subscription",
                                size=14,
                                color="#9ca3af"
                            )
                        ], expand=True, spacing=2),
                        ft.IconButton(
                            icon=ft.Icons.LOGOUT,
                            icon_color="#ef4444",
                            tooltip="Sign Out",
                            on_click=lambda _: self.show_login()
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=ft.padding.all(20),
                    margin=ft.margin.only(bottom=20)
                ),

                # Status card
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.VERIFIED if has_subscription else ft.Icons.WARNING_AMBER,
                                    size=28,
                                    color=ft.Colors.WHITE
                                ),
                                bgcolor="#10b981" if has_subscription else "#f59e0b",
                                width=50,
                                height=50,
                                border_radius=25,
                                alignment=ft.alignment.center
                            ),
                            ft.Column([
                                ft.Text(
                                    "Premium Active" if has_subscription else "Free Plan",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE
                                ),
                                ft.Text(
                                    "All features unlocked" if has_subscription else "Upgrade to unlock premium features",
                                    size=14,
                                    color="#d1d5db"
                                ),
                                ft.Text(
                                    f"Expires: {subscription_end.strftime('%B %d, %Y')}" if has_subscription and subscription_end else "",
                                    size=12,
                                    color="#9ca3af"
                                ) if has_subscription else ft.Container()
                            ], expand=True, spacing=2)
                        ], spacing=15)
                    ]),
                    bgcolor="#10b981" if has_subscription else "#f59e0b",
                    padding=ft.padding.all(25),
                    border_radius=16,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.with_opacity(0.2, "#10b981" if has_subscription else "#f59e0b")
                    ),
                    margin=ft.margin.only(bottom=30)
                ),

                # Action buttons
                ft.Column([
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Upgrade to Premium" if not has_subscription else "Manage Subscription",
                            icon=ft.Icons.STAR if not has_subscription else ft.Icons.SETTINGS,
                            on_click=lambda _: self.show_subscribe(),
                            style=ft.ButtonStyle(
                                bgcolor="#6366f1",
                                color=ft.Colors.WHITE,
                                elevation=0,
                                shape=ft.RoundedRectangleBorder(radius=12),
                                padding=ft.padding.symmetric(vertical=18, horizontal=20)
                            ),
                            width=float('inf')
                        ),
                        margin=ft.margin.only(bottom=15)
                    ) if not has_subscription else ft.Container(),

                    # Features list
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Premium Features",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER
                            ),
                            *[
                                ft.Row([
                                    ft.Icon(
                                        ft.Icons.CHECK_CIRCLE,
                                        size=16,
                                        color="#10b981" if has_subscription else "#6b7280"
                                    ),
                                    ft.Text(
                                        feature,
                                        size=14,
                                        color="#d1d5db" if has_subscription else "#9ca3af",
                                        expand=True
                                    )
                                ]) for feature in [
                                    "Unlimited access to all features",
                                    "Priority customer support",
                                    "Advanced analytics",
                                    "Custom integrations",
                                    "No advertisements"
                                ]
                            ]
                        ], spacing=12),
                        bgcolor="#111111",
                        padding=ft.padding.all(20),
                        border_radius=16,
                        border=ft.border.all(1, "#1f1f1f")
                    )
                ], spacing=0)
            ], scroll=ft.ScrollMode.AUTO),
            padding=ft.padding.all(30),
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#0a0a0a", "#111111"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            )
        )

        self.page.add(main_container)
        self.page.update()

    def show_subscribe(self):
        self.clear_page()

        plans = [
            {"name": "Monthly", "price": "$9.99", "period": "/month", "months": 1, "popular": False,
             "color": "#6366f1"},
            {"name": "Quarterly", "price": "$24.99", "period": "/quarter", "months": 3, "popular": True,
             "color": "#8b5cf6", "save": "Save 17%"},
            {"name": "Annual", "price": "$79.99", "period": "/year", "months": 12, "popular": False, "color": "#10b981",
             "save": "Save 33%"}
        ]

        main_container = ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color="#6b7280",
                            on_click=lambda _: self.show_main_app()
                        ),
                        ft.Column([
                            ft.Text(
                                "Choose Your Plan",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE
                            ),
                            ft.Text(
                                "Unlock premium features",
                                size=14,
                                color="#9ca3af"
                            )
                        ], expand=True, spacing=2)
                    ]),
                    padding=ft.padding.all(20),
                    margin=ft.margin.only(bottom=20)
                ),

                # Plans
                *[
                    ft.Container(
                        content=ft.Column([
                            # Popular badge
                            ft.Container(
                                content=ft.Text(
                                    "MOST POPULAR",
                                    size=10,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE
                                ),
                                bgcolor="#ec4899",
                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                border_radius=12,
                                alignment=ft.alignment.center
                            ) if plan['popular'] else ft.Container(height=0),

                            ft.Column([
                                ft.Row([
                                    ft.Column([
                                        ft.Text(
                                            plan['name'],
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE
                                        ),
                                        ft.Text(
                                            plan.get('save', ''),
                                            size=12,
                                            color="#10b981"
                                        ) if plan.get('save') else ft.Container()
                                    ], expand=True),
                                    ft.Column([
                                        ft.Row([
                                            ft.Text(
                                                plan['price'],
                                                size=24,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE
                                            ),
                                            ft.Text(
                                                plan['period'],
                                                size=14,
                                                color="#9ca3af"
                                            )
                                        ], spacing=5)
                                    ])
                                ]),

                                ft.Container(
                                    content=ft.ElevatedButton(
                                        text="Choose Plan",
                                        on_click=lambda _, m=plan['months']: self.purchase_subscription(m),
                                        style=ft.ButtonStyle(
                                            bgcolor=plan['color'],
                                            color=ft.Colors.WHITE,
                                            elevation=0,
                                            shape=ft.RoundedRectangleBorder(radius=10),
                                            padding=ft.padding.symmetric(vertical=12)
                                        ),
                                        width=float('inf')
                                    ),
                                    margin=ft.margin.only(top=15)
                                )
                            ], spacing=15)
                        ], spacing=10),
                        bgcolor="#111111" if not plan['popular'] else plan['color'] + "20",
                        padding=ft.padding.all(20),
                        border_radius=16,
                        border=ft.border.all(2 if plan['popular'] else 1,
                                             plan['color'] if plan['popular'] else "#1f1f1f"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(0.1 if not plan['popular'] else 0.2, plan['color'])
                        ),
                        margin=ft.margin.only(bottom=15)
                    ) for plan in plans
                ]
            ], scroll=ft.ScrollMode.AUTO),
            padding=ft.padding.all(30),
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#0a0a0a", "#111111"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            )
        )

        self.page.add(main_container)
        self.page.update()

    def login(self, e):
        username = self.username_field.value
        password = self.password_field.value

        if not username or not password:
            self.show_snack_bar("Please enter both username and password", "error")
            return

        if not self.db:
            self.show_snack_bar("Database connection failed", "error")
            return

        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, username, subscription_end FROM users WHERE username = %s AND password = %s",
            (username, password)
        )
        user = cursor.fetchone()

        if user:
            self.current_user = user
            self.show_main_app()
        else:
            self.show_snack_bar("Invalid username or password", "error")

    def register(self, e):
        username = self.reg_username_field.value
        email = self.reg_email_field.value
        password = self.reg_password_field.value

        if not username or not email or not password:
            self.show_snack_bar("Please fill in all fields", "error")
            return

        if len(password) < 6:
            self.show_snack_bar("Password must be at least 6 characters", "error")
            return

        if not self.db:
            self.show_snack_bar("Database connection failed", "error")
            return

        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            if cursor.fetchone():
                self.show_snack_bar("Username or email already exists", "error")
                return

            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            self.db.commit()
            self.show_snack_bar("Account created successfully!", "success")
            self.show_login()
        except Exception as e:
            self.show_snack_bar(f"Registration failed: {e}", "error")

    def purchase_subscription(self, months):
        if not self.db:
            self.show_snack_bar("Database connection failed", "error")
            return

        try:
            from dateutil.relativedelta import relativedelta
            subscription_end = datetime.now() + relativedelta(months=months)

            cursor = self.db.cursor()
            cursor.execute(
                "UPDATE users SET subscription_end = %s WHERE id = %s",
                (subscription_end, self.current_user['id'])
            )
            self.db.commit()
            self.show_snack_bar(f"Premium subscription activated for {months} month(s)!", "success")
            self.show_main_app()
        except ImportError:
            # Fallback if dateutil is not available
            try:
                current_date = datetime.now()
                new_month = current_date.month + months
                new_year = current_date.year + (new_month - 1) // 12
                new_month = ((new_month - 1) % 12) + 1
                subscription_end = current_date.replace(year=new_year, month=new_month)

                cursor = self.db.cursor()
                cursor.execute(
                    "UPDATE users SET subscription_end = %s WHERE id = %s",
                    (subscription_end, self.current_user['id'])
                )
                self.db.commit()
                self.show_snack_bar(f"Premium subscription activated for {months} month(s)!", "success")
                self.show_main_app()
            except Exception as e:
                self.show_snack_bar(f"Failed to activate subscription: {e}", "error")
        except Exception as e:
            self.show_snack_bar(f"Failed to activate subscription: {e}", "error")

    def show_snack_bar(self, message, message_type="info"):
        colors = {
            "success": "#10b981",
            "error": "#ef4444",
            "info": "#6366f1"
        }

        snack_bar = ft.SnackBar(
            content=ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=colors.get(message_type, colors["info"]),
            duration=3000
        )
        self.page.show_snack_bar(snack_bar)

    def __del__(self):
        if hasattr(self, 'db') and self.db and self.db.is_connected():
            self.db.close()


if __name__ == "__main__":
    # Install required packages
    import subprocess
    import sys

    try:
        import flet
        import mysql.connector
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "flet", "mysql-connector-python", "python-dateutil"])
        import flet
        import mysql.connector

    app = SubscriptionApp()
    ft.app(target=app.main)