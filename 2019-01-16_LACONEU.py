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
# figpath_etienne = os.path.join(home, 'pool/EtienneRey')
# figpath_sparse = os.path.join(home, 'pool/science/Perrinet2015BICV_sparse/figures')
# figpath_bednar = os.path.join(home, 'pool/science/PerrinetBednar15/talk')
# figpath_bednar2 = os.path.join(home, 'pool/science/PerrinetBednar15/figures')
# figpath_méjanes = os.path.join(home, 'pool/blog/invibe/output/files/2016-04-28_méjanes/figures')
# figpath_FLE = os.path.join(home, 'ownCNRS/2018-03-26_cours-NeuroComp_FEP/figures')
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
            'Sparse coding',
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

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hi, I am Laurent Perrinet from (LOGO) the Institute de Neurosciences de la Timone in Marseille, a joint unit from the CNRS and AMU. Using computational models, I am investigating the link between the efficiency of behavioural responses in vision, their underlying neural code and their adaptation to the structure of the world.

* (SHOW TITLE - THEME) = mon but ici est de montrer quelques aspects de mon projet de recherche et en particulier des echos de ces tracaux que nous avons realiséavec Etienne Rey
please interrupt

""")

s.add_slide(content=s.content_figures([figname], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes=" All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU
* (OBJECTIVE) in this talk, I will be focus in highlighting
some key challenges in understanding visual perception
in terams of efficient coding
using modelization and neural data and
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

so what is visual perception?
""")


review_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="http://invibe.net/LaurentPerrinet/Publications/Perrinet15bicv">Biologically Inspired Computer Vision</a>')

figpath = os.path.join(home,  'pool/science/BICV/bicv.github.io/images')
s.add_slide(image_fname=os.path.join(figpath, 'bicv_banner.jpg'),
            content=s.content_figures(
                    [os.path.join(figpath, 'bicv_cover.jpg')],
                    title=None, height=s.meta['height']*.85)+review_bib,
            notes="""
... by linking to the statistics of natural images:

* (natural) For instance, oriented edges that constitute images of natural scenes
tend to be aligned in co-linear or co-circular arrangements, such as when
💠 you follow the contours of these boulders: lines and smooth curves
are more common than other possible arrangements of edges. See for example
the work of Mariano Sigman on co-circularity in natural images (see Sigman, 2001).

* (neural) The visual system appears to take advantage of this prior
information, and human contour detection and grouping performance is well
predicted by what is coined an "association field" (Field et al., 1993)...
""")


figpath = os.path.join(home,  'pool/science/RetinaClouds/')
s.add_slide(content="""
    <video controls loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, '2016-09-14_droplets_round2/data_cache/2016-09-14_frames/00004_droplets_i_sparse_0_seed_1973.mp4'))),
            notes="""


""")

droplets_bib = s.content_bib('Ravello, Escobar, Palacios, LP', '2019', 'in prep', url=None)
figpath = os.path.join(home, 'science/DropLets/figures/')
s.add_slide(content=s.content_figures(
                    [os.path.join(figpath, 'retina_sparseness_droplets.png'),
                     os.path.join(figpath, 'PSTH11.png'),
                     os.path.join(figpath, 'PSTH25.png')],
                    title=None, height=s.meta['height']*.85)+droplets_bib,
            notes="""
figure 3 of droplets

""")

figpath = os.path.join(home,  'RetinaCloudsSparse/2015-11-13_droplets/2015-11-13_1310_full_files/droplets_full')
for fname in ['00012_droplets_i_sparse_3_n_sf_8.mp4', '00006_droplets_i_sparse_5_n_sf_1.mp4']:
    s.add_slide(content="""
        <video controls loop width=99%/>
          <source type="video/mp4" src="{}">
        </video>
        """.format(s.embed_video(os.path.join(figpath, fname))),
                notes="""


    """)

figpath = os.path.join(home, 'pool/science/PerrinetBednar15/talk/')
# anatomical
s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'Bosking97Fig4.jpg')], title=None,
            height=s.meta['height']*.85) +
            s.content_bib("Bosking et al.", "1997", " Journal of Neuroscience"),
            notes="""
... is the set of long-range lateral connections between neurons, which could
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

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Sparse coding  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section)

figpath = os.path.join(home,  'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join('figures', 'MP.mp4'))))

figpath = os.path.join(home, 'pool/science/PerrinetBednar15/figures/')
srep_bib = s.content_bib("LP and Bednar", "2015", 'Scientific Reports, <a href="http://www.nature.com/articles/srep11400">http://www.nature.com/articles/srep11400</a>')
s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'figure_synthesis.jpg')], bgcolor="white",
        title=None, height=s.meta['height']*.85) + srep_bib,
           notes="""

We first extracted the edges from images using a scale-space analysis (all OSS
on github) The histogram was computed as a a 4-dimensional function of
distance, (symmetrical) azimuth $\psi$, difference of orientation $\theta$ and
ratio of scale. ... second-order statistics are efficiently computed by using a
the algorithm from Geisler et al. (2001), with a more general edge extraction
algorithm that uses sparse coding %to avoid multiple responses to a single
edge.  * ... Collinearity and co-circularity results for natural images
replicated qualitatively the results from Geisler et al. (2001), confirming
that prior information about continuations appeared consistently in natural
images.

Probability distribution function of "chevrons" * (angles)  By computing
measures of the independence of the different variables, we found that the
probability density function of the second-order statistics of edges factorizes
with on one side distance and scale and on the other side the 2 angles.  The
first component proved to be quite similar across both classes and the greater
difference is seen for different angle configuration. As it can be reduced to 2
dimensions, we can plot the full probability as shown here by different
contrast values assigned to all possible chevrons configurations, for all
possible "azimuth" values $\psi$ on the horizontal axis and difference of
orientation $\theta$ on the vertical axis. Such a plot most strikingly shows
the difference between these 2 classes.  one issue now that we can show the 2nd
order statistics is to know if it would be possible to quantify such
difference...

* (colin)  let's first replicate the result from Geisler by showing that
relative to a given edge (segment in the center), what is the Here I show for
each distance and angle the most probable difference of angle, showing that
collinear and parallel edges predominate.  (cocir) a similar pattern is observed the
cocircular plot. it reproduces the results from Geisler on natural images, but
laboratory environment shows a strong bias to colinearity. If we believe
bosking link, obviously, this should have a consequence on antomy. thus we test
whether these AF were different across different image classes.
""")

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         Sparse Hebbian Learning - 15''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section)


figpath = os.path.join(home,  'quantic/2016_science/2014-04-17_HDR/figures/')
s.add_slide(content="""
    <video controls loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, 'ssc.mp4'))))
for suffix in ['_a', '_ab', '']:
    s.add_slide(content=s.content_figures(
        [os.path.join('figures', 'figure_sparsenet' + suffix + '.png')], bgcolor="black",
        title=None, height=s.meta['height']*.7) + review_bib,
           notes="""

discussion...

""")

figpath = os.path.join(home,  'quantic/2016_science/2017-01-19_BICV_sparse/figures/')
figpath = os.path.join(home,  'pool/science/BICV/SHL_scripts/')


for suffix in ['_nohomeo', '_homeo']:

    s.add_slide(content=s.content_figures(
        [os.path.join('figures', 'fig_laughlin.png'), os.path.join(figpath, 'ssc' + suffix + '.png')], bgcolor="black",
        title=None, list_of_weights=[1., 2.], height=s.meta['height']*.85) + review_bib,
       notes="""



""")

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 STDP - 15''  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section)
s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "fig_sup_stdps.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8),
          notes="""

#  /Users/laurentperrinet/nextcloud/RTC/2019-01-11\ rapport\ M2A\ HL\ 5bf69490a5705a15960895d6/Figures/fig_sup_stdps.pdf

""")

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "hugoladret_InternshipM2_FINAL_1_couche.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8),
          notes="""

# https://github.com/hugoladret/InternshipM2/blob/master/FINAL_1_couche.ipynb

""")


# FINAL_L2_noshift.pdf
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
