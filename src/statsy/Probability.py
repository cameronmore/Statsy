from .main import *

def simple_probability(desired_outcomes:str,total_outcomes:str)->Number:
    """
    Returns the probability of a set of outcomes A out of the number of all equally likely outcomes B. \n
    """
    return desired_outcomes / total_outcomes

def joint_probability(a:Number,b:Number)->Number:
    """
    Returns the joint probability of A and B where A and B are independent outcomes. \n
    Formula: P (A and B) = P (A) X P (B) \n
    Also known as conjunctive probability. \n
    """
    return a * b

def bare_joint_probability(a_desired:Number,a_possible:Number,b_desired:Number,b_possible:Number)->Number:
    """
    Returns the joint probability of A and B where A and B are independent outcomes and P(A) and P(B) must be calculated. \n
    Formula: P (A and B) = P (A) X P (B) \n
    Where P(A) and P(B) are not known. \n
    """
    return simple_probability(a_desired,a_possible) * simple_probability(b_desired,b_possible)

def disjunctive_probability(P_of_a:Number,P_of_b:Number,P_of_a_and_b:Optional[Number]=None):
    """
    Returns the disjunctive probability of A where A and B are independent outcomes. \n
    Formula: P (A or B) = P (A) + P (B) - P (A and B) \n
    Where P(A) , P(B), and P(A and B) is known.
    """
    jp = joint_probability(P_of_a,P_of_b)
    if P_of_a_and_b is not None:
        jp = P_of_a_and_b
    return P_of_a + P_of_b - jp

def bare_disjunctive_probability(a_desired:Number,a_possible:Number,b_desired:Number,b_possible:Number)->Number:
    """
    Returns the disjunctive probability of A where A and B are independent outcomes. \n
    Formula: P (A or B) = P (A) + P (B) - P (A and B) \n
    Where P(A) and P(B) are not known. \n
    """
    P_of_a = simple_probability(a_desired,a_possible)
    P_of_b = simple_probability(b_desired,b_possible)
    jp = joint_probability(P_of_a,P_of_b)
    return P_of_a + P_of_b - jp
