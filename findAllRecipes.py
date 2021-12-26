class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        supplySet = set(supplies)
        ret = []
        recipeDict = dict()
        recipeCheck = dict()
        for recipe,ingredient in zip(recipes,ingredients):
            recipeDict[recipe] = ingredient
            recipeCheck[recipe] = -1
        def findRecipe(recipe,ingredient,stack=set()):
            if recipeCheck[recipe] == True:
                return True
            elif recipeCheck[recipe] == False:
                return False
            enough = True
            for m in ingredient:
                if m not in supplySet:
                    if m in recipeDict:
                        if m in stack: # check if there is a loop
                            enough = False
                            break
                        else:
                            stack.add(recipe)
                            enough = findRecipe(m,recipeDict[m],stack)
                            if not enough:
                                break
                    else:                            
                        enough = False
                        break
            if enough:
                recipeCheck[recipe] = True
            else:
                recipeCheck[recipe] = False
            return enough
        for recipe,ingredient in zip(recipes,ingredients):
            findRecipe(recipe,ingredient,set())
        for recipe in recipes:
            if recipeCheck[recipe] == True:
                ret.append(recipe)
        return ret
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat","burger"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
sol = Solution()
print(sol.findAllRecipes(recipes,ingredients,supplies))

