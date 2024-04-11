class WellsScoreInstance(self):
   def __init__(self, dvt, pe, hr, surgery_immobilised, haemoptysis, hx):


   def give_advice(self):


   def get_score_breakdown(self):

      print(
         "Welcome to the Two-level PE Wells Score.\nThis score is used to estimate the clinical probability of pulmonary embolism and inform further investigations and management. Please input Y or N to the following questions.")

      wells_score = 0

      # Question 1
      while True:
         clin_feat = input("Are there clinical features of deep vein thrombosis?\n")

         if clin_feat.lower() == "y":
            wells_score += 3
            break
         elif clin_feat.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Question 2

      while True:
         alt_diag = input("Is an alternative diagnosis less likely than PE?\n")

         if alt_diag.lower() == "y":
            wells_score += 3
            break
         elif alt_diag.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Question 3

      while True:
         HR = input("What is the patient's heart rate?\n")
         try:
            HR = int(HR)
         except ValueError:
            print("You did not enter an integer. Please enter an integer.")
         else:
            if int(HR) > 100:
               wells_score += 1.5
               break
            else:
               break

      # Question 4

      while True:
         immob = input("Has the patient been immobilised for 3 days or had surgery in the previous 4 weeks?\n")

         if immob.lower() == "y":
            wells_score += 1.5
            break
         elif immob.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Question 5

      while True:
         immob = input("Has the patient had a previous DVT or PE?\n")

         if immob.lower() == "y":
            wells_score += 1.5
            break
         elif immob.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Question 6

      while True:
         haemop = input("Does the patient have haemoptysis?\n")
         if haemop.lower() == "y":
            wells_score += 1
            break
         elif haemop.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Question 7

      while True:
         cancer = input(
            "Does the patient have a past medical history of cancer and is receiving treatment, has been treated in the last 6 months or is being managed palliatively?\n")

         if cancer.lower() == "y":
            wells_score += 1
            break
         elif cancer.lower() == "n":
            break
         else:
            print("You did not enter Y or N. Please enter Y or N to proceed.")

      # Advice

      print("\n-------------------------------------------\nThe Wells score is " + str(Wells_score) + "/12.5")

      if wells_score > 4:
         print("Given that the Wells score is more than 4, PE is likely. Please arrange hospital admission.")
         while True:
            CTPA = input("Can CTPA be carried out immediately?\n")
            if CTPA.lower() == "y":
               print("Proceed with CTPA as soon as possible.")
               break
            elif CTPA.lower() == "n":
               print(
                  "Offer interim therapeutic anticoagulation (if possible, choose an anticoagulant that can be continued if PE is confirmed). Proceed with CTPA as soon as possible.")
               break
            else:
               print("You did not enter Y or N. Please enter Y or N to proceed.")

      else:
         print(
            "Given that the Wells score is 4 or less, PE is unlikely. Offer a D-dimer test with the results available within 4 hours.\n")

         print(
            "If the D-dimer test result cannot be obtained within 4 hours, offer interim therapeutic anticoagulation while awaiting the result (if possible, choose an anticoagulant that can be continued if PE is confirmed).\n")

         print(
            "If the D-dimer test is positive:\nArrange admission to hospital for an immediate CTPA and, where necessary, other investigations. If CTPA cannot be carried out immediately, offer interim therapeutic anticoagulation (if possible, choose an anticoagulant that can be continued if PE is confirmed)\n")

         print(
            "If the D-dimer test is negative:\nStop interim therapeutic anticoagulation (if appropriate).\nAdvise the person that it is not likely that they have a PE, but discuss the signs and symptoms, and when they should seek further medical help.\nConsider an alternative diagnosis.")
