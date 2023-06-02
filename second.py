from prefect import flow,task

from prefect.blocks.system import String

string_block = String.load("firstblock")

@task
def my_task():
    bob ='print me'
    return(bob)
    
@flow
def subflow_task():
    man ='print'
    return(man)


@flow(name="f w t")
def my_flow():
    subflow =subflow_task()
    task = my_task()

#if __name__ == "main":
my_flow()  

