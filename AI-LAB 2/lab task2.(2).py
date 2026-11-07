Delivery_Robot = {
    "Observability": "Partially Observable",
    "Type": "Stochastic",
    "Observable Variable": "GPS location",
    "Hidden Variable": "Pedestrian behind obstacles",
    "Predictable Outcome": "Brakes reduce robot speed",
    "Uncertain Outcome": "Pedestrian may cross suddenly",
    "Justification": "Robot cannot observe all surroundings and traffic is unpredictable"
}

Student_Agent = {
    "Observability": "Partially Observable",
    "Type": "Stochastic",
    "Observable Variable": "Student question",
    "Hidden Variable": "Student understanding",
    "Predictable Outcome": "Same FAQ gives the same stored answer",
    "Uncertain Outcome": "LLM may generate different answers",
    "Justification": "Agent has incomplete student information and responses may vary"
}


Real_Environment = "Partially Observable and Stochastic"



Simulator = "Fully Observable and Deterministic"

Assumptions = [
    "Simulator has fixed variables and predefined outcomes",
    "Robot uses fixed routes and obstacles",
    "Student agent uses fixed questions and answers"
]

print(Delivery_Robot)
print(Student_Agent)
print(Real_Environment)
print(Simulator)