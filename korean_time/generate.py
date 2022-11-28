from google.cloud import texttospeech

CLIENT = texttospeech.TextToSpeechClient.from_service_account_json('./google-api-credentials.json')
NATIVE = ' 한 두 세 네 다섯 여섯 일곱 여덟 아홉'.split(' ')
SINO = ' 일 이 삼 사 오 육 칠 팔 구'.split(' ')


def to_korean(h, m):
    text = ''
    if h >= 10:
        text += '열'
    text += NATIVE[h % 10] + '시 '
    if m == 30:
        return text + '반'
    if m >= 20:
        text += SINO[m // 10]
    if m >= 10:
        text += '십'
    if m >= 1:
        text += SINO[m % 10] + '분'
    return text


def get_mp3(text, language_code):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    return CLIENT.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config).audio_content


for hour in range(1, 13):
    for minute in range(60):
        with open(f'mp3s/{str(hour).zfill(2)}:{str(minute).zfill(2)}.mp3', 'wb') as fh:
            fh.write(get_mp3(to_korean(hour, minute), 'ko-KR'))
