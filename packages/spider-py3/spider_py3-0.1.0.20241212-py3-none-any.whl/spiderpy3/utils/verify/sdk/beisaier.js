// t(b-a) + a
// tb -at + a
// (1-t)a + tb
// lerp(a,b,t)

// P0 P1
// (1-t)P0 + tP1
// lerp(P0,P1,t)

// P0 P1 P2
// lerp(P0,P1,t) lerp(P1,P2,t)
// lerp(lerp(P0,P1,t),lerp(P1,P2,t),t)
// lerp((1-t)P0 + tP1, (1-t)P1 + tP2,t)
// (1-t)((1-t)P0 + tP1) + t((1-t)P1 + tP2)
//