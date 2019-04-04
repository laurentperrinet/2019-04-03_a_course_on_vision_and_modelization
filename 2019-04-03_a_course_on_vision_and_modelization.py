__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
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

from academic import slugify

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
 draft = False, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 # reveal_path='http://laurentperrinet.github.io/slides.py/',
 reveal_path='',
 theme='simple',
 bgcolor="white",
 author='Perrinet, Laurent U',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugify(tag)}/">Laurent Perrinet</a>',
 short_title='From the retina to action: Understanding visual processing',
 title='From the retina to action: <BR> Understanding visual processing',
 conference_url='https://pluri-sciences.univ-amu.fr/licence-sciences-humanites',
 short_conference='Licence Sciences & Humanité',
 conference='Licence Sciences & Humanité',
 location='Marseille (France)',
 abstract="""Visual areas are essential in transforming the raw luminous signal into a representation which efficiently conveys information about the environment. This process is constrained by various factors such as a wide variety of changes in the characteristics of the visual image but also by the necessity to be able to respond as quickly as possible to the incoming sensory stream, for instance to drive a movement of the eyes to the location of a potential danger. To achieve this, it is believed that the visual system takes advantage of the existence of a priori knowledge in the structure of visual information, such as the regularity in the shape and motion of visual objects. We will review different models around the predictive coding coding framework to offer a unified theory to explain many of the mechanisms at the different levels of the visual system and which were unveiled by decades of study in neurophysiology and psychophysics.""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='anr-horizontal-v1',
 time_start = '16:00:00',
 time_end = '18:00:00',
 url=f'https://laurentperrinet.github.io/talk/{slugify(tag)}',
 sections=['From the retina to action: Levels of modeling',
          'Sparse coding in neurophysiology and models',
          'Modeling Spiking Neural Networks',
          'A model of Sparse Deep Predictive Coding',
          ]
)


# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname_qr = os.path.join(figpath_talk, 'qr.png')
if not os.path.isfile(figname_qr):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname_qr, scale=5)

print(meta['sections'])
s = Slides(meta)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 From the retina to action: Levels of modeling  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 0
s.open_section()
###############################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>

<small>
    This work was supported by ANR project "Horizontal-V1" N° ANR-17-CE37-0006".
</small>
""".format(**meta)
###############################################################################
# s.add_slide(content=intro)
#
# s.add_slide(content=s.content_figures(
#     #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
#     [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
#     height=s.meta['height']*1.),
#     #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
#     notes="""
# Check-list:
# -----------
#
# * (before) bring VGA adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
#  """)
#
#
# s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
#             notes="All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU

* (OBJECTIVE)
Today I will present some recent results on Predictive processing in the visual system ... in visual systemS /
From the retina to action

* please interrupt

* (ACKNO) this endeavour involves different techniques and tools ...
From the head on, I wish to thanks people who collaborated  and in particular ..
  mostly funded by the ANR horizontal V1 (fregnac chavane)
+ LONDON (Jim Bednar, Friston)

* (SHOW TITLE)

""")

Churchland92_bib = s.content_bib("Churchland, P. S. & Sejnowski, T. J.", "1992", 'The computational brain. Cambridge, MA: MIT Press.')
sejnowski88_bib = s.content_bib("Sejnowski, T. J.  &  Koch, C.  & Churchland, P. S.", "1988", 'Computational Neuroscience.', url="http://www.hms.harvard.edu/bss/neuro/bornlab/nb204/papers/sejnowski-koch-churchland-science1988.pdf")

for si in ['', ]:#, '5dh']:
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, 'Churchland92' + si + '.png')], title=None, embed=False, height=s.meta['height']*.7) + Churchland92_bib,
            notes="""

Screenshot from Craver, C. F. (2015). Levels. In T. Metzinger & J. M. Windt (Eds). Open MIND: 8(T). Frankfurt am Main: MIND Group. doi: 10.15502/9783958570498 24 | 26


""")
#

    # open questions:
    #figpath = '../2017-03-06_cours-NeuroComp_intro/figures'
    bib =  '(see this <a href=" http://viperlib.york.ac.uk/areas/15-anatomy-physiology/contributions/2032-hubel-and-wiesel">viperlib</a> page)'

    for fname in ['scientists.jpg']:
        s.add_slide(content=s.content_figures(
           [os.path.join(figpath_talk, fname)], cell_bgcolor=meta['bgcolor'],
           title=meta['sections'][i_section], height=s.meta['height']*height_ratio) + bib,
            notes="""

* (INTRO) Indeed, a conundrum in visual neuroscience, and neuroscience in general, is to infer the causes that underly the firing of any given neural cell. in visual neuroscience, this is conceptualized by the term of receptive field [[---a concept which dates back to Sherrington and to the scratch reflex of the dog---]] and which corresponds to the set of visual stimuli that causes the firing of any given neuron, this set being guessed by changing the parameters of the visual stimulation,
 * to illustrate this methodology, I love to see this picture of David Hubel and Torsten Wiesel performing their Nobel Prize-winning experiments on area V1.  ( source: http://viperlib.york.ac.uk/areas/15-anatomy-physiology/contributions/2032-hubel-and-wiesel ) -
 """)

    s.add_slide(content="""
        <video controls width=90%/>
          <source type="video/mp4" src="{}">
        </video>
        <BR>
        """.format(s.embed_video(os.path.join(figpath_talk, 'ComplexDirSelCortCell250_title.mp4'))) + bib,
    notes="""
on the video, they characterize a complex cell from area V1 by manipulating the visual stimulation's parameters: central position, orientation of a bar, direction, ...
* -> As a consequence,  Neurons are often characterized using simple stimuli like bars or grating
    """)



    # anatomical
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, 'Bosking97Fig4.jpg')], title=None, height=s.meta['height']*.85) +
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


    # figpath = os.path.join(home, 'tmp/2015_RTC/2014-12-31_PerrinetAdamsFriston14/poster/12-06-25_AREADNE/')
    freemove_bib = s.content_bib("LP, Adams and Friston", "2015", 'Biological Cybernetics', url="http://invibe.net/LaurentPerrinet/Publications/PerrinetAdamsFriston14")

    #for fname in ['figure1.png', 'figure2.png']:
    # figpath_law = os.path.join(home, 'quantic/2016_science/2016-10-13_LAW/figures')
    for fname, note in zip(['friston_figure2.png', 'friston_figure1.png'], ["""
* This schematic shows the dependencies among various quantities modelling exchanges of an agent with the environment. It shows the states of the environment and the system in terms of a probabilistic dependency graph, where connections denote directed (causal) dependencies. The quantities are described within the nodes of this graph -- with exemplar forms for their dependencies on other variables.

* Hidden (external) and internal states of the agent are separated by action and sensory states. Both action and internal states -- encoding a conditional probability density function over hidden states -- minimise free energy. Note that hidden states in the real world and the form of their dynamics can be different from that assumed by the generative model; (this is why hidden states are in bold. )
""","""
*  Active inference uses a generalisation of Kalman filtering to provide Bayes optimal estimates of hidden states and action in generalized coordinates of motion. As we have seen previously, the central nervous system has to contend with axonal delays, both at the sensory and the motor levels. Representing hidden states in generalized coordinates provides a simple way of compensating for both these delays.

* This mathematical framework can be mapped to the anatomy of the visual system. Similar to the sketch that we have shown above, "compiling" (that is, solving) the equations of Free-energy minimization forms a set of coupled differential equations which correpond to different node along the visuo-oculomotor pathways.
"""]):
        s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, fname)], bgcolor="white",
    #title=title,
     height=s.meta['height']*height_ratio) + freemove_bib,
    notes=note)
s.close_section()

# >>> Lup IS HERE <<<

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Sparse coding in Neurophysiology and neural processing  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""


""")


ravello_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="http://invibe.net/LaurentPerrinet/Publications/Perrinet15bicv">Biologically Inspired Computer Vision</a>')
# $ o /Users/laurentperrinet/pool/blog/laurentperrinet.github.io_sciblog/files/2019-01-30_Ravello19_text.mp4
# /Users/laurentperrinet/pool/blog/hugo_academic/content/publication/ravello-19
ravelllo_bib = s.content_bib('Ravello, LP, Escobar, Palacios', '2019', 'Scientific Reports', url='https://laurentperrinet.github.io/publication/ravello-19/')

figpath = os.path.join(home, 'pool/blog/laurentperrinet.github.io_sciblog/files/')
figpath = os.path.join(home, 'pool/blog/hugo_academic/content/publication/ravello-19')
s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, 'video_perrinet.mp4'))) + ravello_bib,
            notes="""
First in the retina, thanks to a collaboration with CR,  MJE and AP in Chile we have studied the response of retinal cells as recorded on grids of electordes in a diurnal rodent, the degu.

... this video shows the type of stimulations that we have shown from classical gratings to noisier texture

""")


for si in ['2', '5ac', '1', ]:#, '5dh']:
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, 'Ravello2018_'+ si + '.png')], title=None, embed=False, height=s.meta['height']*.7) + ravelllo_bib,
            notes="""
figure 3 of MS1

... surprisingly as shown here, retinal responses get sparser with complexity: the selectivity to speed in particular gets sharper for broadband stimuli.

it may seem counter intuitive, but makes sense: gratings contain only one frequency - it's "poor"" while natural images contain a wider range of information


""")
#
# s.add_slide(content=s.content_figures(
#     [os.path.join(figpath_talk, 'featured.jpg')], bgcolor="white", embed=False,
#     title=None, height=s.meta['height']*.85) + ravello_bib,
#             notes="""
# ... surprisingly as shown here, retinal responses get sparser with comlpexity: the selectivity to speed in particular gets sharper for broadband stimuli.
#
# it may seem counter intuitive, but makes sense: gratings contain only one frequency - it's "poor"" while natural images contain a wider range of information
#
# """)


jens_bib = s.content_bib("Kremkow, LP, Monier, Alonso, Aertsen, Fregnac, Masson", "2016", 'Push-pull receptive field organization and synaptic depression: Mechanisms for reliably encoding naturalistic stimuli in V1', url='https://laurentperrinet.github.io/publication/kremkow-16/')
jens_url = 'https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/'
jens_url = 'figures/'
# for l in ['a', 'b', '']:
for l in ['a', '']:
    s.add_slide(content=s.content_figures(
        [jens_url + 'fncir-10-00037-g001' + l + '.jpg'], bgcolor="white",
        title=None, embed=False, height=s.meta['height']*.8) + jens_bib,
           notes="""
there are many more evidences for this and in particular, we have modeled that for the ... cat's cortex following recordings done in Yves Fregnac's lab

""")

# https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/fncir-10-00037-g004.jpg
# https://www.frontiersin.org/files/Articles/190318/fncir-10-00037-HTML/image_m/fncir-10-00037-g005.jpg
# s.add_slide(content=s.content_figures(
#         [jens_url + 'fncir-10-00037-g004.jpg', jens_url + 'fncir-10-00037-g005.jpg'], bgcolor="white", fragment=True,
#         title=None, embed=False, height=s.meta['height']*.8) + jens_bib,
#            notes="""
#
# for this, we had
#
#
# such processing seems also extend to action
# """)



review_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="http://invibe.net/LaurentPerrinet/Publications/Perrinet15bicv">Biologically Inspired Computer Vision</a>')
#
# figpath = os.path.join(home, 'science/invibe/2018_visuels')
# s.add_slide(content="""
#     <video controls loop width=60%/>
#       <source type="video/mp4" src="{}">
#     </video>
#     """.format(#'figures/MP.mp4'), #
#                 s.embed_video(os.path.join(figpath, 'MP.mp4'))),
#             notes="""
# ... this video shows this intuition in a quantitative way. from a natural image,
# we extracted independent sources as individual edges at different scales and
# orientations
#
# when we reconstruct this image frame by frame (see N)
# we can quickly recognize the image
#
# natural images are sparse
# """)

# figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=85%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/v1_tiger.mp4') + review_bib, #s.embed_video(os.path.join(figpath,     """.format(s.embed_video(os.path.join(figpath_talk, 'v1_tiger.mp4'))),
notes="""

hypothesis= structural prior that one can learn

same procedure with retinal filters (scale, no orientation) = sparseness
""")


#
# ols_bib = s.content_bib("Olshausen and Field", "1997", 'Sparse coding with an overcomplete basis set: A strategy employed by V1?')
# for i in [2]:
#     s.add_slide(content=s.content_figures(
#         [os.path.join(figpath_talk, 'Olshausen_'+ str(i) + '.png')], bgcolor="white",
#         title=None, embed=False, height=s.meta['height']*.85) + ols_bib,
#            notes="""
# since we assume the retina would invert this model, let's use the forward model
# to generate stimuli = droplets
#
# """)

ols_bib = s.content_bib("Olshausen and Field", "1997", 'Sparse coding with an overcomplete basis set: A strategy employed by V1?')
for i in [1, 2, 5]:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'Olshausen_'+ str(i) + '.png')], bgcolor="white", embed=False,
        title=None, height=s.meta['height']*.85) + ols_bib, #+ f' <small>{ols_bib}<\small> ',
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


shl_bib = s.content_bib("LP", "2010", 'Neural Computation', url="https://laurentperrinet.github.io/publication/perrinet-10-shl/")

s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/ssc.mp4') + shl_bib )

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Modeling Spiking Neural Networks  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""

Can we now go to a lower level and model spiking NNs?

""")

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "HH_neuron.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8) +
            s.content_bib("Hodgkin & Huxley", "1952", "The Journal of physiology"),
          notes="""

          http://www.math.tamu.edu/~roquesol/Computational_Neuroscience_Summer_I_2018_Session_2-3_Print.pdf

""")


s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "HH_Models.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8),
          notes="""

""")


# https://brian2.readthedocs.io/en/stable/_static/brian-logo.png
# http://www.nest-initiative.org/wp-content/uploads/2015/03/nest-initiative_logo.png
# http://neuralensemble.org/docs/PyNN/0.7/_static/pyNN_logo.png
s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "brian-logo.png"),
         os.path.join(figpath_talk, "nest-initiative_logo.png"),
         os.path.join(figpath_talk, "pyNN_logo.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.4),
          notes="""

""")

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "HH_firing.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8),
          notes="""
# ownCNRS/2019-01_LACONEU/2019-01-14_LACONEU/tmp/4-HH Models.ipynb
ownCNRS/2019-01_LACONEU/2019-01-14_LACONEU/A_1_HodgkinHuxley.ipynb
HH_firing.png
""")
#
# s.add_slide(content=s.content_figures(
#         [os.path.join(figpath_talk, "IF_cond_exp.png"), ], bgcolor="black",
#         title=None, height=s.meta['height']*.8),
#           notes="""
#
# # http://neuralensemble.org/docs/PyNN/0.7/_images/IF_cond_exp.png
#
# """)

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "izhik.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8) +
            s.content_bib("Izhikevich", "2003", "IEEE Transactions on Neural Network", url="https://www.izhikevich.org/publications/spikes.htm"),
          notes="""

#

""")


for figname in ['Brunel200Fig2.png', 'Brunel200Fig1.png']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, figname), ], bgcolor="black",
        title=None, height=s.meta['height']*.8) +
            s.content_bib("Brunel", "2000", "Neurocomputing", url="https://sci-hub.tw/https://doi.org/10.1016/S0925-2312(00)00179-X"),
          notes="""


# https://sci-hub.tw/https://doi.org/10.1016/S0925-2312(00)00179-X

""")

for fig_OBV1, h in [('2_Figure_psychophys', .9), ('Fig_intro_MC1', .61), ('Fig_intro_MC2', .61), ('Fig_ring_model', .99) ]:
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, fig_OBV1 + ".png"), ], bgcolor="black",
            title=None, height=s.meta['height']*h),
              notes="""
    /Users/laurentperrinet/research/OBV1/2018_HL_M1/figs

    """)

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "hugoladret_InternshipM2_CUBA.png"), ], bgcolor="black",
        title=None, height=s.meta['height']*.8),
          notes="""

# https://github.com/hugoladret/InternshipM2/blob/master/FINAL_Retina_LGN_generation.ipynb

""")


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

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 DEEP LEARNING  A model of Sparse Deep Predictive Coding      🏄🏄🏄🏄🏄🏄🏄🏄
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

one can go one step before the cortex and ask the same question in the retina
are the same process present ?


Theoretical advances in neural networks modelling have recently been pushed by the field of machine learning. These have proposed that biological neural networks could process information according to certain constraints of efficiency, such as minimizing the surprise of sensory states given noisy or ambiguous sensory inputs. We have developed such a Hierarchical (Deep) Predictive Coding model using unsupervised learning on (static) natural images, and that we wish to extend to (dynamic) sensory flows. Compared to classical Deep Learning models, one advantage of this approach is that the learned synaptic weights are meaningful, that is that they often emerge as to represent explicitly components of the input image in increasing levels of complexity: edges at the first layer, curvatures in the second, the eye or mouth in the third layer when presenting images of faces. Such networks can also be extended to supervised or reinforcement learning by adding efferent layers that would accept such labels.
#

""")



SDPC_bib = s.content_bib('Boutin, Franciosini, Ruffier, LP', '2019', 'submitted',
            url="https://laurentperrinet.github.io/publication/boutin-franciosini-ruffier-perrinet-19/")

for suffix in ['_a']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'boutin-franciosini-ruffier-perrinet-19_figure1' + suffix + '.png')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*.85)+SDPC_bib,
           notes="""

figure 1 of SDPC

research/NN-2018

""")

CNN_ref = '(from <a href="http://cs231n.github.io/convolutional-networks/">http://cs231n.github.io/convolutional-networks/</a>)'
s.add_slide(content=s.content_figures(
    ['http://cs231n.github.io/assets/cnn/depthcol.jpeg'], bgcolor="black",
title=None,  embed=False, height=s.meta['height']*.85) + CNN_ref,
       notes="""

this can be extended to a convolutional neural networks

""")


for suffix in ['_a', '_b', '_c', '']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'boutin-franciosini-ruffier-perrinet-19_figure1' + suffix + '.png')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*.85)+SDPC_bib,
           notes="""

figure 1 of SDPC

cf. research/NN-2018

""")

s.add_slide(content="""
    <video controls loop width=85%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/training_video_ATT.mp4'),
    notes="""

    Let's now apply that to natural images of faces

    """)
# 20190206-Training of the SDPC model on AT&T database-0CFrmgEcGpw.f135.mp4

for suffix in ['4a', '4b']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'boutin-franciosini-ruffier-perrinet-19_figure' + suffix + '.png')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*.85),
           notes="""

Multi-layered unsupervised Learning

Figure 4: Input, features and reconstructed input after the training on the AT&T database.(a) Images pre-processed with Local Contrast Normalization [36]. (b) 32 randomly selectedfirst-layer RFs fromD(1).  (c) First-layer reconstruction, generated by back-projectingγ1into  the  input  space.   (d)  64  second-layer  RFs  (randomly  selected)  of  size  28×28  px,drawn from the effective dictionaryD(2).  (e) Second-layer reconstruction, generated byback-projectingγ2into the input space, showing 3 best examples (left) and the 3 worst.

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

# The free parameters of this network are the anatomical constraints that we impose to dimension layers. In the particular case of this networks, this is the number of layers, the number of channels (that is the number of overlays of the same map in a given layer), and the size of the kernels implementing the convolutions (in resemblance to receptive fields in biological NNs). Indeed, as in most classical Deep Learning neural networks, these parameters are hand tuned. However, we observed that these superstructural numbers have a great influence on the quality and type of filters that could emerge from the learning phase.  Theoretically, this make sense as it imposes different levels of competition within each layer across channels but also by defining a characteristic size in local interactions.
# We believe that this theoretical problem is similar to that faced by different the primary visual cortex in different species. Given a similar sensory input, the intra-cortical network imposes different levels of anatomical complexities. We predict that, given realistic orders of magnitudes for different species, we could differentially predict the emergence of different macrostructures in different species. In particular, the emergence of a topographically smooth representation of orientations is present in marmosets while mice have a salt-and-pepper representation. Thanks to this level of understanding, we will use our models to make predictions. In particular, we can generate images which are optimal to evoke activity targeted at a given layer, for instance for the second layer (curvatures) versus the first layer (edges). In practice, such images take the form of textures with different levels of structural complexity. For instance, stimuli targeted at the first layer would correspond to a sub-class of stimuli that we have widely used in previous experiments (Motion Clouds). We predict that more complex classes of stimuli should evoke differential activities in both species.

# - Task 5: Bluesky: “Efficient hierarchical representations ” Overall, the role of visual information processing in cortical layers is to represent information robustly to noise and visual transformations (translations zooms rotations). There is thus a pressure on the structure of this processing at different temporal scales to maximize the efficiency of this code. This depends both on the statistics of the sensory input (both in space and time) but also on the repertoire of behavioral tasks that are embodied. We have recently developed a hierarchical unsupervised algorithm for neural networks which allows to generate such representations and that fits well to the processing performed by feed-forward, lateral and feedback connections. In such a model, the message passing between neurons is implemented by propagating waves which progressively refine the representation of sensory data. In particular, tuning the complexity of the representation at different layers allows to see the emergence of different structures. In particular, progressively increasing the complexity in lateral connections shows a phase transition from a salt-and-pepper organization to a more continuous representation of the space x orientation space. This could explain the different architectures observed in different animals. Such models could also make predictions on the adaptation of the network to novel environmental or behavioral contingencies.  The goal of this Task is two-sided: first to understand the physiological and behavioral data in the light of predictive coding theories, rooting these results in a quantitative model. The second goal is to generate predictions. In particular, using our models, it will be possible to generate novel stimulus classes that specifically tackle the efficiency of the visual system at its different spatial and dynamic granularities. Lead Laurent/Lyle?
#

* Thanks for your attention!
""")



s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code ")

s.close_section()



if slides_filename is None:
    with open("README.md", "w") as text_file:
        text_file.write("""\
# {title}

* Where: {location}, see {url}
* When: {DD:02d}/{MM:02d}/{YYYY}, time: {time_start}-{time_end}

* What:
  * Slides @ https://laurentperrinet.github.io/{tag}
  * Code for slides @ https://github.com/laurentperrinet/{tag}/
  * Abstract: {abstract}

""".format(**meta))

    with open("/tmp/talk.bib", "w") as text_file:
        text_file.write("""\
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}",
    Title = "{title}",
    Abstract = "{abstract}",
    Url = "{url}",
    Year = "{YYYY}",
    Date = "{YYYY}-{MM:02d}-{DD:02d}",
    location = "{location}",
    projects = "{projects}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_start}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_end}",
    url = "{url}",
    url_slides = "https://laurentperrinet.github.io/{tag}",
    url_code = "https://github.com/laurentperrinet/{tag}/",
}}

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
