from mplsoccer import Pitch


def pitch_image():
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#1e1e1e', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
    fig.set_facecolor('#1e1e1e')
    fig.savefig('/Users/jordanpickles/Library/CloudStorage/OneDrive-Personal/Personal Data Projects/UnderstatData/Football Pitch.png', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    pitch_image()