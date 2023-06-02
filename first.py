from prefect import flow

@flow
def my_favorite_function():
    print("What is your favorite number?")
    return 42

print(my_favorite_function())





# @task
# def printer(obj):
#     print(f"Received a {type(obj)} with value {obj}")

# # note that we define the flow with type hints
# @flow
# def validation_flow(x: int, y: str):
#     printer(x)
#     printer(y)

# validation_flow(x="42", y=100)



from prefect import flow

@flow(name="mussie flow")
def my_flow():
    print('don pablooo')