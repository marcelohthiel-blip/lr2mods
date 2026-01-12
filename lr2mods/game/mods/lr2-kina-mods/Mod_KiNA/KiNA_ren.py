from math import floor
import renpy
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.character_related.JobDefinition_ren import JobDefinition
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
#from game.major_game_classes.business_related.Business_ren import Business 
#from game.major_game_classes.business_related.Infraction_ren import Infraction
#from game.game_roles._role_definitions_ren import employee_role 
#from game.major_game_classes.game_logic.Role_ren import Role
#from game.game_roles.business_roles._duty_definitions_ren import general_duties_list, general_hr_duties, general_supply_duties, general_market_duties, general_rd_duties, general_production_duties, hr_work_duty, market_work_duty, research_work_duty, head_researcher_duty, production_work_duty, supply_work_duty, daily_serum_dosage_duty


"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
def kina_decorate_run_day():
    #Making it harder to increase baby desire
    undecorated_run_day = Person.run_day
    def decorated_function(self,*args,**kwargs):
        #Run the vanilla "run_day" actions.
        undecorated_run_day(self,*args,**kwargs)
        #disable the base game's changes first
        if persistent.pregnancy_pref == 3:
        #Only on realistic setting
            if self.love > self.baby_desire + 20:
                self.change_baby_desire(-1) #base game add 1 if love > 20 so we takes it back       
            #Now we update the baby desire ...
            kidsmult = self.kids * 5 #More kids, the higher happiness threshold needed to have another  
            kidsvar = self.kids * 10 #She more reluctant to have more kids if she already have several 
            if self.happiness > 130 + kidsmult:
                if self.love > self.baby_desire + kidsvar:  #Start game, Mom needs at least 60 love and 140 happiness before she even +baby desire
                    self.change_baby_desire(1)
                    #mc.log_event(self.title + " dreamt of having a baby", "float_text_grey")
            elif self.happiness < 120 + kidsmult:
                if not self.has_breeding_fetish:
                    self.change_baby_desire(-1)
                    #mc.log_event(self.title + " having nightmare of getting pregnant", "float_text_grey")

            #Child Support
            # If child support enabled AND have given birth AND a week have passed since last payment
            if child_support_enabled and (self.has_event_day("last_birth") and self.days_since_event("child_support") >= 7): 
                self.set_event_day("child_support")
                pay_cs_amount = self.number_of_children_with_mc * cs_amount
                mc.business.change_funds(-pay_cs_amount, stat = "Family Support")
                if self.number_of_children_with_mc == 0:
                    mc.log_event(f"{self.name} {self.last_name} : {self.possessive_title} not entitled to your child support.", "float_text_grey")
                elif self.number_of_children_with_mc == 1:
                    mc.log_event(f"{self.name} {self.last_name} : {self.possessive_title} received ${pay_cs_amount} in child support for {self.number_of_children_with_mc} child.", "float_text_grey")
                else:
                    mc.log_event(f"{self.name} {self.last_name} : {self.possessive_title} received ${pay_cs_amount} in child support for {self.number_of_children_with_mc} children.", "float_text_grey")
            elif self.has_event_day("last_birth") and not self.has_event_day("child_support"):
                # Recently gave birth AND NOT yet set to receive payment 
                mc.log_event(f"{self.name} {self.last_name} - Recently gave birth.", "float_text_grey")
                self.set_event_day("child_support")
        
        #Happiness boost. The base game normalize toward 100 which is below smiling threshold. The only way the girls gains happiness is totally dependant through interactions with player.
        #Yet, they will lose happiness especially those that had poor opinion on Friday, weekend and Monday. Thus, after 2 weeks, they falls into depression if you didnt interact with them
        if self.love > 10 and self.happiness < 130: #This allow up to 140 happiness with 100 love.
            amount = builtins.int(builtins.round(self.love/10))
            self.change_happiness(amount, add_to_log = False)
            #mc.log_event(self.title + "'s happiness buff by " + str(amount), "float_text_grey")
        #elif self.love < 0 and self.happiness < 130: #Haters be happy hating
        #    amount = 1 + builtins.int(builtins.round(abs(self.love)/10)) 
        #    self.change_happiness(amount, add_to_log = False)
        #    mc.log_event(self.title + "'s happiness hate buff by " + str(amount), "float_text_grey")

        #Employee Skill up -- Thanks Kaden + seronis on LR2R discord on the tips ... 
        if auto_skill_enabled and self.is_employee and (self.has_event_day("skill_update") and self.days_since_event("skill_update") >= skill_check_delay): #TIER_3_TIME_DELAY*2):
            #Only our main company employee
            self.set_event_day("skill_update")

            job = self.primary_job

            if job.job_definition in mc.business.research_jobs and self.research_skill < 8:
                mc.log_event(f"Autoskill : Evaluating {self.name} {self.last_name}'s research skill and relevant stats", "float_text_grey")
                if renpy.random.randint(0, self.research_skill) == self.research_skill :
                    self.change_research_skill(1)
                if not self.personality == bimbo_personality and renpy.random.randint(0, self.int*2) == self.int and self.int < 8:
                    self.change_int(1)
                if renpy.random.randint(0, self.focus*2) == self.focus and self.focus < 8 :
                    self.change_focus(1)
            elif job.job_definition in mc.business.market_jobs and self.market_skill < 8:
                mc.log_event(f"Autoskill : Evaluating {self.name} {self.last_name}'s market skill and relevant stats", "float_text_grey")
                if renpy.random.randint(0, self.market_skill) == self.market_skill :
                    self.change_market_skill(1)
                if renpy.random.randint(0, self.charisma*2) == self.charisma and self.charisma < 8 :
                    self.change_cha(1)
                if renpy.random.randint(0, self.focus*2) == self.focus and self.focus < 8 :
                    self.change_focus(1)
            elif job.job_definition in mc.business.supply_jobs and self.supply_skill < 8:
                mc.log_event(f"Autoskill : Evaluating {self.name} {self.last_name}'s supply skill and relevant stats", "float_text_grey")
                if renpy.random.randint(0, self.supply_skill) == self.supply_skill :
                    self.change_supply_skill(1)
                if renpy.random.randint(0, self.charisma*2) == self.charisma and self.charisma < 8 :
                    self.change_cha(1)
                if renpy.random.randint(0, self.focus*2) == self.focus and self.focus < 8 :
                    self.change_focus(1)
            elif job.job_definition in mc.business.production_jobs and self.production_skill < 8:
                mc.log_event(f"Autoskill : Evaluating {self.name} {self.last_name}'s production skill and relevant stats", "float_text_grey")
                if renpy.random.randint(0, self.production_skill) == self.production_skill :
                    self.change_production_skill(1)
                if not self.personality == bimbo_personality and renpy.random.randint(0, self.int*2) == self.int and self.int < 8:
                    self.change_int(1)
                if renpy.random.randint(0, self.focus*2) == self.focus and self.focus < 8 :
                    self.change_focus(1)
            elif job.job_definition in mc.business.hr_jobs and self.hr_skill < 8:
                mc.log_event(f"Autoskill : Evaluating {self.name} {self.last_name}'s hr skill and relevant stats", "float_text_grey")
                if renpy.random.randint(0, self.hr_skill) == self.hr_skill :
                    self.change_hr_skill(1)
                if renpy.random.randint(0, self.charisma*2) == self.charisma and self.charisma < 8 :
                    self.change_cha(1)
                if not self.personality == bimbo_personality and renpy.random.randint(0, self.int*2) == self.int and self.int < 8:
                    self.change_int(1)
        elif self.is_employee and not self.has_event_day("skill_update"):
            #Recently hired
            mc.log_event(f"{self.name} {self.last_name} - Recently hired.", "float_text_grey")
            self.set_event_day("skill_update")
            
        
                
    Person.run_day = decorated_function
kina_decorate_run_day()