from random import shuffle
from sender import Sender

def shuffle_and_verify(seq):
    """Shuffle a list and verify that it is not the same."""
    old_seq = list(seq)
    while seq == old_seq:
        shuffle(seq)
    return seq

def distributeSantas(participants,server,email,password):
    shuffle_and_verify(participants)

    client = Sender(server, email, password)
    client.login()

    f = open('matches.txt', 'w')

    for i in range(len(participants)):
        giver = participants[i]
        getter = participants[(i + 1) % len(participants)]
        f.write(giver[0] + ' --> ' + getter[0] + '\n')
        client.send(
            giver[1], 'Secret Santa',
            'Your match is: %s' % getter[0]
        )

    f.close()
    client.logout()
