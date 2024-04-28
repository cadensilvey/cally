# from flet import *

# class EnterScores(UserControl):
#     def __init__(self, page, hole_pars):
#         super().__init__()
#         self.page = page
#         self.hole_pars = hole_pars
#         self.current_hole = 1
#         self.hole_scores = [0] * 18
#         self.input_element = TextField(
#             label=f"Enter Score for Hole {self.current_hole}",
#             on_change=lambda _: self.hole_input_changed()
#         )

#     def btn_click(self, e):
#         if not self.input_element.value.isdigit():
#             self.input_element.error_text = "Please enter a valid number"
#             self.update()
#         else:
#             self.hole_scores[self.current_hole - 1] = int(self.input_element.value)
#             self.next_hole_clicked()

#     def next_hole_clicked(self):
#         if self.current_hole < 18:
#             self.current_hole += 1
#             self.input_element.label = f"Enter Score for Hole {self.current_hole}"
#             self.input_element.value = str(self.hole_scores[self.current_hole - 1])
#             self.update()
#         else:
#             self.submit_scores()

#     def submit_scores(self):
#         print("Scores for each hole:", self.hole_scores)
#         print("Pars for each hole:", self.hole_pars)

#         # Compare scores against pars
#         for hole_num, (score, par) in enumerate(zip(self.hole_scores, self.hole_pars), start=1):
#             if score < par:
#                 print(f"You scored {score} on Hole {hole_num}, which is under par!")
#             elif score == par:
#                 print(f"You scored par {score} on Hole {hole_num}.")
#             else:
#                 print(f"You scored {score} on Hole {hole_num}, which is over par.")

#     def build(self):
#         return Column(
#             controls=[
#                 Container(
#                     height=1000,
#                     width=1000,
#                     padding=10,
#                     margin=10,
#                     bgcolor='#fdebd3',
#                     content=Column(
#                         controls=[
#                             Container(
#                                 content=Text(
#                                     f"Enter Score for Hole {self.current_hole}",
#                                     theme_style=TextThemeStyle.DISPLAY_MEDIUM
#                                 ),
#                                 margin=10,
#                                 padding=10,
#                             ),
#                             Row(
#                                 [
#                                     Text("Score:"),
#                                     self.input_element
#                                 ],
#                             ),
#                             ElevatedButton(
#                                 "Submit",
#                                 on_click=lambda _: self.submit_scores()
#                             ),
#                             ElevatedButton(
#                                 "Next Hole",
#                                 on_click=lambda _: self.next_hole_clicked()
#                             ),
#                             ElevatedButton(
#                                 "Back",
#                                 on_click=lambda _: self.page.go('/type')
#                             ),
#                         ]
#                     )
#                 )
#             ]
#         )

#     def hole_input_changed(self):
#         value = self.input_element.value
#         if not value.isdigit():
#             self.input_element.error_text = "Please enter a valid number"
#         else:
#             self.input_element.error_text = ""
#             self.hole_scores[self.current_hole - 1] = int(value)
