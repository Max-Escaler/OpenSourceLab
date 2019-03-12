#Lab6

1. Shortest path between chaos and order is
chaos
chats
coats
colts
colas
codas
codes
coder
cider
eider
elder
older
order
Shortest path between nodes and graph is
nodes
modes
moles
molds
golds
goads
grads
grade
grape
graph
Shortest path between pound and marks is
None
Shortest path between moron and smart is
moron
boron
baron
caron
capon
capos
capes
canes
banes
bands
bends
beads
bears
sears
stars
start
smart


2. def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    fh = gzip.open('words4_dat.txt.gz', 'r')
    words = set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:4])
        words.add(w)
    return generate_graph(words)
3. Shortest path between cold and warm is
cold
cord
word
worm
warm
Shortest path between love and hate is
love
hove
have
hate

4. 