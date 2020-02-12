import pampy as pm

# str_in = str(input())


def edit(str_in):
    str_out = pm.match(str_in,
                       ('a',pm._), lambda _: ('b',_))

assert edit("s") == "SS"
assert edit(" s") == " S"
assert edit("a") == "b"
assert edit(" sas") == " Sbss"