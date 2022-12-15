function draw() {}

function set_walls() {}

function sand() {}


const points = [];
let endpoints;
let xmin = xmax = 500;
let ymax = 0;

for (line of f) {
    endpoints = line.split(" -> ").map(p => p.split(",").map(Number));
    const xs = endpoints.map(p => p[0]);
    const ys = endpoints.map(p => p[1]);
    xmin = Math.min(xmin, ...xs);
    xmax = Math.max(xmax, ...xs);
    ymax = Math.max(ymax, ...ys);
    points.push(endpoints);
}

const floorx = [500-ymax-3, 500+ymax+3];
const floory = ymax + 2;
const floor = [[floorx[0], floory], [floorx[1], floory]];

console.log(points[0]);