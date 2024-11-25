from sympy import symbols, Eq, ForAll, Implies, simplify_logic
x, y = symbols('x y')
is_mammal= symbols('IsMammal', cls=True)
has_fur= symbols('HasFur', cls=True)
knowledge_base = []
while True:
    predicate= input("Enter a predicate (e.g., 'IsMammal', 'HasFur'): ")
    if not predicate:
        break 
    variable=  symbols(input("Enter a variable for predicate (predicate)': "))
    predicate_symbol=symbols(predicate, cls=True)       
    statement=predicate_symbol(variable)
    knowledge_base.append(statement)

query= input("Enter a query (e.g., 'IsMammal(x)', 'HasFur(y)'): ") 
query_predicate=eval(query.split('(')[0])
conclusion = None
for statement in knowledge_base:
    if statement.equals(query_predicate):
        conclusion = "Yes, the query can be inferred from the knowledge base."
        break
    else:
        conclusion = "No, the query cannot be inferred from the knowledge base."

print(conclusion)