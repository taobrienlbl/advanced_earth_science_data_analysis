import generate_frame
from simplempi.parfor import parfor, pprint

# loop in parallel over all files
for i in parfor(range(720)):
    pprint(f"working on {i}")
    generate_frame.generate_frame(
        i,
        output_dir = "./animation_frames_alternate"
        )