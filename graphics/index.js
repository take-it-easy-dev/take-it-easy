var MAIN_DOT_UP_COLOR = "red";
var MAIN_DOT_LEFT_COLOR = "green";
var MAIN_DOT_RIGHT_COLOR = "blue";

var ALLOWED_UP_COLORS = ["gold", "red", "turquise"];
var ALLOWED_LEFT_COLORS = ["gray", "purple", "black"];
var ALLOWED_RIGHT_COLORS = ["yellow", "blue", "green"];

TAKEN_FIELDS = new Set();

function reset_taken_fields() {
    TAKEN_FIELDS = new Set();
}

function set_field(input_id) {
    if (!TAKEN_FIELDS.has(input_id)) {
        TAKEN_FIELDS.add(input_id);
        const newUpClassName = `rect up ${MAIN_DOT_UP_COLOR}`;
        const newLeftClassName = `rect left ${MAIN_DOT_LEFT_COLOR}`;
        const newRightClassName = `rect right ${MAIN_DOT_RIGHT_COLOR}`;
        document.getElementById(`dot${input_id} up`).className = newUpClassName;
        document.getElementById(`dot${input_id} left`).className = newLeftClassName;
        document.getElementById(`dot${input_id} right`).className = newRightClassName;
        generate_new_main_dot();
    }
}

function change_main_dot_color(direction, color) {
    const elementId = `main-dot-${direction}-rect`;
    document.getElementById(elementId).className = `rect-big ${direction} ${color}`;
    if (direction === "up") {
        MAIN_DOT_UP_COLOR = color;
    }
    else if (direction === "left") {
        MAIN_DOT_LEFT_COLOR = color;
    }
    else if (direction == "right") {
        MAIN_DOT_RIGHT_COLOR = color;
    }
}

function _generate_random_color_index() {
    return Math.floor(Math.random() * 3);
}

function generate_new_main_dot() {
    MAIN_DOT_UP_COLOR = ALLOWED_UP_COLORS[_generate_random_color_index()];
    MAIN_DOT_LEFT_COLOR = ALLOWED_LEFT_COLORS[_generate_random_color_index()];
    MAIN_DOT_RIGHT_COLOR = ALLOWED_RIGHT_COLORS[_generate_random_color_index()];

    change_main_dot_color('up', MAIN_DOT_UP_COLOR);
    change_main_dot_color('left', MAIN_DOT_LEFT_COLOR);
    change_main_dot_color('right', MAIN_DOT_RIGHT_COLOR);
}