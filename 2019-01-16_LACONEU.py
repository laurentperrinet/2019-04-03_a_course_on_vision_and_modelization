#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False

import os
home = os.environ['HOME']
figpath_talk = 'figures'
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
#
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .7

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.7.0/',
 theme='simple',
 bgcolor="white",
 author='Laurent Perrinet, INT',
 author_link='<a href="http://invibe.net">Laurent Perrinet</a>',
 short_title='Efficient coding of visual information in neural computations',
 title='Efficient coding of visual information in neural computations',
 conference_url='http://www.laconeu.cl',
 short_conference='LACONEU 2019',
 conference='LACONEU 2019: 5th Latin-American Summer School in Computational Neuroscience',
 location='Valparaiso (Chile)',
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 url='http://invibe.net/LaurentPerrinet/Presentations/' + tag,
 abstract="""
""",
wiki_extras="""
----
<<Include(BibtexNote)>>
----
<<Include(AnrHorizontalV1Aknow)>>
----
TagYear{YY} TagTalks [[TagAnrHorizontalV1]]""".format(YY=str(YYYY)[-2:]),
sections=['Efficiency, vision and neurons',
          'Sparse coding in the retina?',
          'Sparse Hebbian Learning']
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname = os.path.join(figpath_talk, 'qr.png')
if not os.path.isfile(figname):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname, scale=5)

print(meta['sections'])
s = Slides(meta)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 intro  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 0
s.open_section()
###############################################################################

s.hide_slide(content=s.content_figures(
    #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
    [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
    height=s.meta['height']*.90),
    #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
    notes="""
Check-list:
-----------

* (before) bring VGA adaptors, AC plug, remote, pointer
* (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
* (VP) open monitor preferences / calibrate / title page
* (timer) start up timer
* (look) @ audience

http://pne.people.si.umich.edu/PDF/howtotalk.pdf

 """)

intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>
""".format(**meta)

s.hide_slide(content=intro)

s.hide_slide(content=s.content_figures([figname], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes=" All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU

* (OBJECTIVE) in this talk, I will be focus in highlighting
some key challenges in understanding visual perception
in terams of efficient coding
using modelization and neural data
* please interrupt

* (ACKNO) this endeavour involves different techniques and tools ...
From the head on, I wish to thanks people who collaborated  and in particular ..
  mostly funded by the ANR horizontal V1
(fregnac chavane) + ANR TRAJECTORY (o marrre bruno cessac palacios )
+ LONDON (Jim Bednar, Friston)

* (SHOW TITLE) I am interested in the link
between the neural code and the structure of the world.
in particular, for vision, I am researching
the relation between the
functional (in terms of the inferential processes leading to  behaviour)
organization (anatomy and activity)
of low-level visual areas (V1) and the structures of natural scenes,
that is of the images that hit the retina and which are
relevant to visual perception in general.

so what is vision efficient? in particular if we look around us,
images are formed by a relatively low number of features, which are arranged
according to prototypical structures - lines, curves, contours
""")


review_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="http://invibe.net/LaurentPerrinet/Publications/Perrinet15bicv">Biologically Inspired Computer Vision</a>')

figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(#'figures/MP.mp4'), #
                s.embed_video(os.path.join(figpath, 'MP.mp4'))),
            notes="""
... this video shows this intuition in a quantitative way. from a natural image,
we extracted independent sources as individual edges at different scales and
orientations

when we reconstruct this image frame by frame (see N)
we can quickly recognize the image

natural images are sparse
""")

ols_bib = s.content_bib("Olshausen and Field", "1997", 'Sparse coding with an overcomplete basis set: A strategy employed by V1?')
for i in [1, 2, 5]:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'Olshausen_'+ str(i) + '.png')], bgcolor="white", embed=False,
        title=None, height=s.meta['height']*.85) + ols_bib,
           notes="""
a seminal idea is proposed by Olshausen:
* this may be formalized as an inference problem:

edges are different sources, which are known to be sparse:
by mixing these sources one forms the image (transparency hypothesis)

the sparseness is characterized by the pdf of the sources coefficients

* this inference problem is an inverse problem:

* while this problem may be hard to solve, this may be approached using
a (conjugate) gradient descent which has a nice implementation in terms of
neural networks

I wish to point here to an essential feature compared to classical feed-forward
networks: you can not do the inference in one single shot in general;
you need a recurrent / recursive network  (see arrow) and this is precisely
a possible function for one of the most numerous type of synapses: short-ranges
lateral interactions

""")



figpath = os.path.join(home, 'pool/science/PerrinetBednar15/talk/')
# anatomical
s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'Bosking97Fig4.jpg')], title=None,
            height=s.meta['height']*.85) +
            s.content_bib("Bosking et al.", "1997", " Journal of Neuroscience"),
            notes="""
in the primary visual cortex for instance,
 the set of long-range lateral connections between neurons, which could
act to facilitate detection of contours matching the association field, and/or
inhibit detection of other contours. To fill this role, the lateral connections
would need to be orientation specific and aligned along contours, * (colin) and
indeed such an arrangement has been found in treeshrew's primary visual
cortex  (Bosking et al., J Neurosci 17:2112-27, 1997)
* (neural) if one looks at  the primary visual area in the occipital lobe of the cortex
using optical imaging as here in the treeshrew by Bosking and colleagues under the
supervision of DF, one could represent the distributed, topographical representation
of orientation selectivity. in (A) and (B) the orientation giving the most response
at each cortical position is represented by hue using the code below from orange for
horizontal to blue for verticals, and typical structures are magnified in (C): stripes
(on the periphery) and pinwheels. You can understand this as a packing of a 3D feature
space on the 2D surface of the cortex.
* (method)  Tree shrew orientation preference maps were obtained using optical imaging.
Additionally, 540 nm light was used to map surface blood vessels used for alignment.
Biocytin was then injected into a specific site in V1 and the animal was sacrificed 16
hours later. Slices of V1 were imaged to locate the biocytin bouton and the surface
blood vessels. The blood vessel information was then used to align the orientation
preference maps with the bouton images giving overlaid information on the underlying
connectivity from the injection site on the animal. The original experiment used a total
of ten cases.
* (lateral) we show here one result of Bosking
which overlay over a map or orientation selectivity the network of lateral connectivity
originating froma group of neurons with similar orientations and position. There is
a structure in this connectivity towards locality (more pronounced for site B) +
connecting iso orientations even on long ranges (A). This type of structure tends
to wire together those neurons that have similar orientations, indicating a prior
to colinearities.
*(colin) ... Overall, a typical assumption that the role of lateral interactions is to
enhance the activity of neurons which are collinear : it is the so-called
**association field** formalized in Field 93, as was for instance modeled neurally in
the work from P. Series or in this version for computer vision
* (physio) is there a match of these structures with the statistics of natural images?
 2) Some authors (Kisvarday, 1997, Chavane and Monier) even say it is weak or
inexistent on a the scale of the area... 1:  Hunt & Goodhill have reinterpreted above data and shown that there is more diversity
than that -
* TRANSITION : my goal here will be to tackle this problem at different levels:
""")



#Jens Kremkow, Laurent U Perrinet, Cyril Monier, Jose-Manuel Alonso, Ad Aertsen, Yves Fregnac, Guillaume S Masson. Push-pull receptive field organization and synaptic depression: Mechanisms for reliably encoding naturalistic stimuli in V1, URL URL2 URL3 . Frontiers in Neural Circuits, 2016

jens_bib = s.content_bib("Kremkow, LP, Monier, Alonso, Aertsen, Fregnac, Masson", "2016", 'Push-pull receptive field organization and synaptic depression: Mechanisms for reliably encoding naturalistic stimuli in V1', url='http://invibe.net/LaurentPerrinet/Publications/Kremkow16')
jens_url = 'https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/'
jens_url = 'figures/'
for l in ['a', 'b', '']:
    s.add_slide(content=s.content_figures(
        [jens_url + 'fncir-10-00037-g001' + l + '.jpg'], bgcolor="white",
        title=None, embed=False, height=s.meta['height']*.8) + jens_bib,
           notes="""

""")

# https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/fncir-10-00037-g004.jpg
# https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/fncir-10-00037-g005.jpg
s.add_slide(content=s.content_figures(
        [jens_url + 'fncir-10-00037-g004.jpg', jens_url + 'fncir-10-00037-g005.jpg'], bgcolor="white", fragment=True,
        title=None, embed=False, height=s.meta['height']*.8) + jens_bib,
           notes="""

""")
s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Sparse coding  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
one can go one step before the cortex and ask the same question in the retina
are the same process present ?
""")

ravelllo_bib = s.content_bib('Ravello, LP, Escobar, Palacios', '2018', 'Scientific Reports', url='https://dx.doi.org/10.1101/350330')
for si in ['2', '1', '5ac', '5dh']:
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, 'Ravello2018_'+ si + '.png')], title=None, embed=False, height=s.meta['height']*.7)+ravelllo_bib,
            notes="""
figure 3 of MS1

""")

# figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=85%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/v1_tiger.mp4'), #s.embed_video(os.path.join(figpath,     """.format(s.embed_video(os.path.join(figpath_talk, 'v1_tiger.mp4'))),
notes="""
same procedure with retinal filters (scale, no orientation) = sparseness
""")


droplets_bib = s.content_bib('Ravello, Escobar, Palacios, LP', '2019', 'in prep', url=None)
s.add_slide(content=s.content_figures(
                    ['figures/Droplets_1.png'], fragment=True, transpose=True,
                    title=None, embed=False, height=s.meta['height']*.8)+droplets_bib,
            notes="""
figure 1 of droplets

""")


ols_bib = s.content_bib("Olshausen and Field", "1997", 'Sparse coding with an overcomplete basis set: A strategy employed by V1?')
for i in [2]:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'Olshausen_'+ str(i) + '.png')], bgcolor="white",
        title=None, embed=False, height=s.meta['height']*.85) + ols_bib,
           notes="""
since we assume the retina would invert this model, let's use the forward model
to generate stimuli = droplets

""")

figpath = os.path.join(home,  'pool/science/RetinaCloudsSparse/2015-11-13_droplets/2015-11-13_1310_full_files/droplets_full')
for fname in ['00012_droplets_i_sparse_3_n_sf_8.mp4', '00006_droplets_i_sparse_5_n_sf_1.mp4', ]:
    s.add_slide(content="""
        <video controls loop width=60%/>
          <source type="video/mp4" src="{}">
        </video>
        """.format(s.embed_video(os.path.join(figpath, fname))),
                notes="""
very sparse to very dense

    """)


droplets_bib = s.content_bib('Ravello, Escobar, Palacios, LP', '2019', 'in prep', url=None)
for suffix in ['a', 'b']:
    s.add_slide(content=s.content_figures(
                    [#os.path.join(figpath, 'retina_sparseness_droplets.png'),
                     os.path.join(figpath_talk, 'Droplets_3_' + suffix + '.png')], fragment=False, transpose=True,
                    title=None, embed=False, height=s.meta['height']*.75)+droplets_bib,
            notes="""
figure 3 of droplets

""")

s.add_slide(content=s.content_figures(
                    ['figures/Droplets_5.png'],
                    title=None, embed=False, height=s.meta['height']*.75)+droplets_bib,
            notes="""
figure 5 of droplets

""")

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         Sparse Hebbian Learning - 15''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
let's move to the second part : learning

the main goal of Olshasuen was not only sparse coding but
the fact that using the sparse code, a simple linear hebbian learning allows
to separate independent sources

""")

figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/ssc.mp4')) #s.embed_video(os.path.join(figpath,         s.embed_video(os.path.join('figures', 'ssc.mp4'))))
#

figpath = os.path.join(home, 'science/ABC/HULK/')

for suffix in ['map', 'HAP']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'figure_' + suffix + '.png')], bgcolor="black",
    title=None, height=s.meta['height']*.75),
           notes="""
a contribution we made to this algorithm is homeostasis



""")
CNN_ref = '(from <a href="http://cs231n.github.io/convolutional-networks/">http://cs231n.github.io/convolutional-networks/</a>)'
s.add_slide(content=s.content_figures(
    ['http://cs231n.github.io/assets/cnn/depthcol.jpeg'], bgcolor="black",
title=None,  embed=False, height=s.meta['height']*.85) + CNN_ref,
       notes="""

this can be extended to a convolutional neural networks

""")

for suffix in ['CNN']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'figure_' + suffix + '.png')], bgcolor="black",
    title=None, height=s.meta['height']*.85),
           notes="""

discussion...

""")

for suffix in ['1', '2a', '2b']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'SDPC_' + suffix + '.png')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*.85),
           notes="""

Multi-layered unsupervised Learning


""")


s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'SDPC_' + suffix + '.png') for suffix in ['3', '4']],
    bgcolor="black", fragment=True,
    title=None, embed=False, height=s.meta['height']*.75),
       notes="""

allows for a better classification as here for MNIST digits
""")
s.close_section()

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
s.add_slide(content=intro,
            notes="""


* Thanks for your attention!
""")
s.close_section()


if slides_filename is None:

    with open("/tmp/wiki.txt", "w") as text_file:
        text_file.write("""\
#acl All:read

= {title}  =

 Quoi:: [[{conference_url}|{conference}]]
 Qui:: {author}
 Quand:: {DD}/{MM}/{YYYY}
 Où:: {location}
 Support visuel:: http://blog.invibe.net/files/{tag}.html


 What:: talk @ the [[{conference_url}|{conference}]]
 Who:: {author}
 When:: {DD}/{MM}/{YYYY}
 Where:: {location}
 Slides:: http://blog.invibe.net/files/{tag}.html
 Code:: https://github.com/laurentperrinet/{tag}/
== reference ==
{{{{{{
#!bibtex
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}, {location}",
    Title = "{title}",
    Url = "{url}",
    Year = "{YYYY}",
}}
}}}}}}
## add an horizontal rule to end the include
{wiki_extras}
""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
