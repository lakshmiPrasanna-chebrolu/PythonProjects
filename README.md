# PythonProjects
The small projects that are learned and implemented for the practical understanding of the language.
<h1> OCR </h1>
<p>OCR -Optical Character Recognition or optical character reader
is the electronic or mechanical conversion of images of typed,
handwritten or printed text into machine-encoded text,
whether from a scanned document, a photo of a document, a scene-photo
or from subtitle text superimposed on an image.
<ul>
<li> The first step of ocr is using a scanner to process the physical form of
  a document </li>

<li>Once all pages are copied , OCR software converts the document into a
  two- color, or black and white version </li>


<li> The scanned -in image or bitmap is analysed for light and dark areas ,
where dark areas are identified as characters that need to be recognised
  and light areas are identified as background </li>
  <li>Pattern recoginition or feature recoginition (PyTesseract)
  </li>
  </ul>
</p>
<h3>Requirements:<br>
  pip3 install PyTesseract
  
</h3>
<h1>Audio S&R
</h1>
<p>Pydub package and speech recognisation packages have been installed.
<br>
  with the help of the Pydub module we segment the audio into parts of some milliseconds that we require make sure the size to of the audio file should not exceed more than 10mb otherwise it might cause error.
  <b> Note:</b> ffmpeg file should be downloaded and the bin path should be added to the  path variable in system.
<ul><li>In speech recognition the audio file we extracted from the the audio clip file is saved as audio-extract.wav which will be used for the recognition of audio using googles api recognize_audio function and converts the audio into text.</li>
  <li><b><i> Requirements:
    </i></b>
    pip3 install pydub <br>
    pip3 install SpeechRecognition
  </li></ul>
</p>
