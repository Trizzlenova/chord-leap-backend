from logic.models import User, Chord, Progression
import json



# def seedUsers():
#   users = [
#   {
#     username: 'trizzlenova@gmail.com',
#     password: 'abc123',
#     full_name: 'Troy',
#     image: 'https://img.memecdn.com/fat-bastard_o_2028391.jpg'
#   },
#   {
#     username: 'cantrollover@rocketmail.com',
#     password: 'abcabc',
#     full_name: 'Bob',
#     image: 'http://realhistoryww.com/world_history/ancient/Misc/Human_Race/Mongoloid_albino_3.JPG'
#   },
#   ]

  # for user in users:
  #   new_user = User.create(user)
  #   new_user.save()
  #   print(new_user)



def seedChords():
  Chord.objects.all().delete()
  chords = [
  {
    'name': 'A min',
    'related_chords': "['D maj', 'C maj', 'A min']",
  },
  {
    'name': 'B min',
    'related_chords': "['A maj', 'C maj', 'E min']",
  },
  ]

  for chord in chords:
    new_chord = Chord(name = chord['name'], related_chords = chord['related_chords'])
    new_chord.save()
    print(new_chord)

seedChords()


