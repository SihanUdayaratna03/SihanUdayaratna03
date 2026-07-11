import random

def generate_circuit_svg():
    width = 1000
    height = 300
    
    # Ultra-premium, minimalist dark aesthetic
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <radialGradient id="bg" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#0a0a0c" />
            <stop offset="100%" stop-color="#000000" />
        </radialGradient>
        
        <style>
            /* Base traces: faint and elegant */
            .trace {{ fill: none; stroke: #27272a; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }}
            .node {{ fill: #000000; stroke: #27272a; stroke-width: 1.5; }}
            
            @keyframes flow {{
                0% {{ stroke-dashoffset: 800; }}
                100% {{ stroke-dashoffset: -800; }}
            }}
            /* Data streaks: bright glowing blue */
            .data {{
                fill: none; stroke: #0ea5e9; stroke-width: 2;
                stroke-dasharray: 40 400;
                stroke-linecap: round;
                animation: flow linear infinite;
            }}
            .data-slow {{
                fill: none; stroke: #6366f1; stroke-width: 2;
                stroke-dasharray: 30 500;
                stroke-linecap: round;
                animation: flow linear infinite;
            }}
        </style>
    </defs>
    
    <!-- Background -->
    <rect width="{width}" height="{height}" fill="url(#bg)" />
    
    <g>
'''
    
    paths = []
    
    def add_left_bus(start_x, start_y, count, spacing, drop, x2_len_base):
        for i in range(count):
            y = start_y + i * spacing
            x_angle_start = start_x  # Constant for perfect parallels!
            y2 = y + drop
            x_angle_end = x_angle_start + abs(drop)
            # stagger the endpoints so they don't form a blocky line
            x_end = x_angle_end + x2_len_base + (i * 15 if drop > 0 else -i * 15)
            
            paths.append({
                'd': f"M -10 {y} H {x_angle_start} L {x_angle_end} {y2} H {x_end}",
                'x': x_end, 'y': y2
            })

    def add_right_bus(start_x, start_y, count, spacing, drop, x2_len_base):
        for i in range(count):
            y = start_y + i * spacing
            x_angle_start = start_x
            y2 = y + drop
            # Drawing right to left means X decreases
            x_angle_end = x_angle_start - abs(drop)
            x_end = x_angle_end - x2_len_base - (i * 15 if drop > 0 else -i * 15)
            
            paths.append({
                'd': f"M 1010 {y} H {x_angle_start} L {x_angle_end} {y2} H {x_end}",
                'x': x_end, 'y': y2
            })

    # Elegantly spaced busses (Clean & Modern)
    add_left_bus(100, 30, 4, 15, 50, 150)
    add_left_bus(160, 130, 3, 15, -40, 90)
    add_left_bus(120, 220, 4, 15, -50, 120)
    add_left_bus(60, 260, 2, 15, -30, 180)
    
    add_right_bus(900, 20, 3, 15, 60, 140)
    add_right_bus(850, 100, 4, 15, 50, 110)
    add_right_bus(800, 180, 3, 15, -40, 160)
    add_right_bus(880, 240, 4, 15, -50, 100)

    # A few long straight lines intersecting
    paths.append({'d': f"M -10 110 H 260", 'x': 260, 'y': 110})
    paths.append({'d': f"M -10 190 H 320", 'x': 320, 'y': 190})
    paths.append({'d': f"M 1010 160 H 700", 'x': 700, 'y': 160})
    paths.append({'d': f"M 1010 220 H 750", 'x': 750, 'y': 220})

    # Render paths
    random.seed(99)
    for p in paths:
        svg += f'        <path class="trace" d="{p["d"]}" />\n'
        svg += f'        <circle class="node" cx="{p["x"]}" cy="{p["y"]}" r="3" />\n'
        
        # 70% chance of active data stream
        if random.random() > 0.3:
            dur = round(random.uniform(3.0, 5.0), 1)
            cls = "data" if random.random() > 0.4 else "data-slow"
            svg += f'        <path class="{cls}" d="{p["d"]}" style="animation-duration: {dur}s;" />\n'

    # Typography
    # Because traces are dark gray (#27272a), white text will pop perfectly without a box!
    svg += f'''
    </g>
    
    <g transform="translate(500, 145)">
        <text x="0" y="-5" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="44" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="6">SIHAN UDAYARATNA</text>
        <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#a1a1aa" text-anchor="middle" letter-spacing="10">AI &amp; MACHINE LEARNING ENGINEER</text>
    </g>
</svg>
'''
    with open('banner.svg', 'w') as f:
        f.write(svg)

if __name__ == '__main__':
    generate_circuit_svg()
