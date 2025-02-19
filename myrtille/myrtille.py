import reflex as rx

# Définir les questions et les réponses
questions = [
    {
        "question": "Dans quelle ville la naissance est prévue ?",
        "options": ["Bruxelles", "Paris", "Bamako"],
        "correct_answers": ["Paris"]
    },
    {
        "question": "A quelle jour correspond la date du terme ?",
        "options": ["Le jour de l'été", "La fête de l'échalotte à Saint-Pol-de-Léon", "La fête de la musique"],
        "correct_answers": ["Le jour de l'été", "La fête de la musique"]
    },
    {
        "question": "Pour quel(s) prénom(s) étions-nous d'accord dès le départ ?",
        "options": ["Masculin", "Féminin", "Les deux", "Aucun des deux"],
        "correct_answers": ["Masculin"]
    },
    {
        "question": "Quel sera son premier moyen de transport ?",
        "options": ["Les vélos de papa et maman", "Une poussette Yoyo", "Une Renault 21 GTS Turbo"],
        "correct_answers": ["Une poussette Yoyo"]
    }
]

class QuizAppState(rx.State):
    answers: dict = {i: [] for i in range(len(questions))}
    image_visible: bool = False
    feedback_message: str = ""

    def check_answers(self):
        print(self.answers)
        all_correct = all(
            set(self.answers[i]) == set(questions[i]["correct_answers"])
            for i in range(len(questions))
        )
        self.feedback_message = "Toutes les réponses sont correctes !" if all_correct else "Certaines réponses sont incorrectes."
        print(self.feedback_message)
        self.image_visible = all_correct

    def update_answer(self, question_index, option, value):
        if value:
            print("Checked")
            self.answers[question_index].append(option)
        else:
            print("Unchecked")
            self.answers[question_index].remove(option)
        self.answers = {k: v for k, v in self.answers.items()}  # Force update

def index():
    return rx.box(
        #rx.heading("Quiz pour savoir si c'est un ptit gars ou une ptite fille", font_size="2em", margin_bottom="1em", text_align="center"),
        rx.vstack(
            rx.text("Répondez à toutes ces questions (plusieurs choix possibles).", font_size="1.2em", margin_top="1em"),
            *[
                rx.box(
                    rx.text(questions[i]["question"], font_size="1.2em", margin_bottom="0.5em"),
                    *[
                        rx.checkbox(
                            option,
                            on_change=lambda value, i=i, option=option: QuizAppState.update_answer(i, option, value),
                            margin_bottom="0.5em"
                        )
                        for option in questions[i]["options"]
                    ],
                    border="1px solid #ddd",
                    padding="1em",
                    border_radius="8px",
                    margin_bottom="1em"
                )
                for i in range(len(questions))
            ],
            rx.text("Si toutes les réponses sont bonnes, vous verrez apparaître une image ci-dessous.", font_size="1.2em", margin_top="1em"),
            rx.button("Vérifier les réponses", on_click=QuizAppState.check_answers, bg="blue", color="white", padding="0.5em 1em"),
            rx.cond(
                QuizAppState.image_visible,
                rx.image(src="Couv_327214.jpg", width="300px", height="auto", margin_top="1em"),
            ),
            #rx.text(QuizAppState.feedback_message, color="green" if QuizAppState.image_visible else "red", font_size="1.2em", margin_top="1em"),
            spacing="4",
            padding="4",
            overflow_y="auto"
        ),
        display="flex",
        justify_content="center",
        align_items="center",
        #height="100vh",  # Utilise toute la hauteur de la fenêtre
        padding="2em",
        overflow_y="auto"
    )

app = rx.App()
app.add_page(index)
#app.compile()
