import random

def generate_circuit_svg():
    width = 1000
    height = 300
    
    # Deep blue and cyan colors mimicking the image
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <defs>
        <radialGradient id="bg" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#142850" />
            <stop offset="100%" stop-color="#0a1128" />
        </radialGradient>
        <style>
            .trace {{ fill: none; stroke: #00f0ff; stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; }}
            .node {{ fill: #0a1128; stroke: #00f0ff; stroke-width: 4; }}
            
            @keyframes flow {{
                to {{ stroke-dashoffset: -1000; }}
            }}
            .data {{
                fill: none; stroke: #ffffff; stroke-width: 4;
                stroke-dasharray: 8 180;
                stroke-linecap: round;
                animation: flow linear infinite;
            }}
        </style>
    </defs>
    <rect width="{width}" height="{height}" fill="url(#bg)" />
    
    <!-- No SVG filters here so GitHub Camo doesn't break it! -->
    <g>
'''
    
    paths = []
    
    def add_left_bus(start_y, count, spacing, x1, drop, x2_len):
        sign = 1 if drop > 0 else -1
        for i in range(count):
            y = start_y + i * spacing
            x_angle_start = x1 - i * spacing * sign
            y2 = y + drop
            x_angle_end = x_angle_start + abs(drop)
            x_end = x_angle_end + x2_len + random.randint(0, 30)
            
            paths.append({
                'd': f"M -10 {y} H {x_angle_start} L {x_angle_end} {y2} H {x_end}",
                'x': x_end, 'y': y2
            })

    def add_right_bus(start_y, count, spacing, x_from_right, drop, x2_len):
        sign = 1 if drop > 0 else -1
        for i in range(count):
            y = start_y + i * spacing
            x_from_right_i = x_from_right - i * spacing * sign
            x_angle_start = 1000 - x_from_right_i
            y2 = y + drop
            x_angle_end = x_angle_start - abs(drop)
            x_end = x_angle_end - x2_len - random.randint(0, 30)
            
            paths.append({
                'd': f"M 1010 {y} H {x_angle_start} L {x_angle_end} {y2} H {x_end}",
                'x': x_end, 'y': y2
            })

    # Density! Matches the image exactly.
    # spacing = 12 for thicker lines to not overlap
    add_left_bus(20, 6, 12, 160, 60, 110)
    add_left_bus(140, 5, 12, 180, -50, 90)
    add_left_bus(230, 5, 12, 110, -70, 160)
    add_left_bus(-10, 3, 12, 250, 40, 60)
    
    add_right_bus(10, 5, 12, 160, 70, 100)
    add_right_bus(120, 7, 12, 180, -40, 130)
    add_right_bus(220, 6, 12, 90, -50, 110)
    add_right_bus(-20, 3, 12, 250, 60, 70)

    # Some pure horizontal lines filling gaps
    for i in range(3):
        y = 110 + i * 12
        x_end = 350 + random.randint(0, 50)
        paths.append({'d': f"M -10 {y} H {x_end}", 'x': x_end, 'y': y})
        
    for i in range(3):
        y = 170 + i * 12
        x_end = 650 - random.randint(0, 50)
        paths.append({'d': f"M 1010 {y} H {x_end}", 'x': x_end, 'y': y})

    # Output paths
    random.seed(123)
    for p in paths:
        svg += f'        <path class="trace" d="{p["d"]}" />\n'
        svg += f'        <circle class="node" cx="{p["x"]}" cy="{p["y"]}" r="5.5" />\n'
        
        # Add glowing data packets to 30% of lines
        if random.random() > 0.7:
            dur = round(random.uniform(2.5, 4.5), 1)
            svg += f'        <path class="data" d="{p["d"]}" style="animation-duration: {dur}s;" />\n'

    # Typography
    svg += f'''
    </g>
    
    <!-- Dark overlay behind text so it's readable -->
    <rect x="230" y="100" width="540" height="100" fill="#0a1128" opacity="0.9" rx="8" />
    
    <g transform="translate(500, 145)">
        <text x="0" y="-5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="44" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="4">SIHAN UDAYARATNA</text>
        <text x="0" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#00f0ff" text-anchor="middle" letter-spacing="8">AI &amp; MACHINE LEARNING ENGINEER</text>
    </g>
</svg>
'''
    with open('banner.svg', 'w') as f:
        f.write(svg)

if __name__ == '__main__':
    generate_circuit_svg()
