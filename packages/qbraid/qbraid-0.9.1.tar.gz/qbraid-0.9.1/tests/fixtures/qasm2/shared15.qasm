OPENQASM 2.0;
include "qelib1.inc";
gate iswap q0,q1 { s q0; s q1; h q0; cx q0,q1; cx q1,q0; h q1; }
qreg q[4];
creg c[4];
h q[0];
h q[1];
h q[2];
h q[3];
x q[0];
x q[1];
y q[2];
z q[3];
s q[0];
sdg q[1];
t q[2];
tdg q[3];
rx(pi/4) q[0];
ry(pi/2) q[1];
rz(3*pi/4) q[2];
p(pi/8) q[3];
sx q[0];
sxdg q[1];
iswap q[2],q[3];
swap q[0],q[2];
swap q[1],q[3];
cx q[0],q[1];
cp(pi/4) q[2],q[3];
measure q -> c;