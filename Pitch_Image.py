from mplsoccer import Pitch, VerticalPitch


def pitch_image():
    pitch = VerticalPitch(pitch_type='statsbomb',corner_arcs=True, half=True, pitch_color='#555555', line_color='#c7d5cc', spot_type='square')
    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
    fig.set_facecolor('#555555')


    fig.savefig('/Users/jordanpickles/Library/CloudStorage/OneDrive-Personal/Personal Data Projects/UnderstatData/Football Pitch.png', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    pitch_image()