<style lang="less">
.discussion-modal {
    h3 {
        margin-top: 0;
    }

    .direct-chat-messages {
        height: auto;
    }
}
</style>

<template>
<modal v-ref:modal :title="title" class="discussion-modal" large
    :class="{'modal-danger': deleting}">
    <div class="modal-body" v-show="!deleting">
        <div class="row">
            <dataset-card class="col-xs-12 col-md-offset-3 col-md-6"
                v-if="discussion.subject | is 'dataset'"
                :datasetid="discussion.subject.id"></dataset-card>
            <reuse-card class="col-xs-12 col-md-offset-3 col-md-6"
                v-if="discussion.subject | is 'reuse'"
                :reuseid="discussion.subject.id"></reuse-card>
        </div>
        <h3>{{ discussion.title }}</h3>
        <div class="direct-chat-messages">
            <div class="direct-chat-msg"
                v-for="message in discussion.discussion">
                <div class="direct-chat-info clearfix">
                    <span class="direct-chat-name pull-left">{{message.posted_by | display}}</span>
                    <span class="direct-chat-timestamp pull-right">{{message.posted_on | dt}}</span>
                </div>
                <img class="direct-chat-img"  :alt="_('User Image')"
                    :src="message.posted_by | avatar_url 40"/>
                <div class="direct-chat-text" v-markdown="message.content"></div>
            </div>
        </div>
    </div>
    <div class="modal-body" v-show="deleting">
        <p class="lead text-center">
            {{ _('You are about to delete this discussion') }}
        </p>
        <p class="lead text-center">
            {{ _('Are you sure?') }}
        </p>
    </div>
    <footer class="modal-footer text-center" v-show="!deleting">
        <form v-if="!discussion.closed" v-el:form>
            <div class="form-group">
                <textarea class="form-control" rows="3"
                    :placeholder="_('Type your comment')"
                    v-model="comment" required>
                </textarea>
            </div>
        </form>
        <button type="button" class="btn btn-danger btn-flat pull-left"
            v-if="$root.me.is_admin" @click="confirm_delete">
            {{ _('Delete') }}
        </button>
        <button type="button" class="btn btn-success btn-flat pull-left"
            @click="comment_discussion" v-if="!discussion.closed">
            {{ _('Comment the discussion') }}
        </button>
        <button type="button" class="btn btn-warning btn-flat pull-left"
            @click="close_discussion" v-if="!discussion.closed">
            {{ _('Comment and close discussion') }}
        </button>
        <button type="button" class="btn btn-primary btn-flat"
            @click="$refs.modal.close">
            {{ _('Close') }}
        </button>
    </footer>
    <footer class="modal-footer text-center" v-show="deleting">
        <button type="button" class="btn btn-warning btn-flat pull-left"
            @click="delete">
            {{ _('Confirm') }}
        </button>
        <button type="button" class="btn btn-danger btn-flat"
            @click="cancel_delete">
            {{ _('Cancel') }}
        </button>
    </footer>
</modal>
</template>

<script>
import API  from 'api';
import Vue from 'vue';
import BaseForm from 'components/form/base-form';
import Modal from 'components/modal.vue';
import DatasetCard from 'components/dataset/card.vue';
import ReuseCard from 'components/reuse/card.vue';

export default {
    name: 'discussion-modal',
    mixins: [BaseForm],
    components: {Modal, DatasetCard, ReuseCard},
    computed: {
        title() {
            return this.deleting ? this._('Confirm deletion') : this._('Discussion');
        }
    },
    data() {
        return {
            discussion: {},
            next_route: null,
            comment: null,
            deleting: false
        };
    },
    events: {
        'modal:closed': function() {
            this.$go(this.next_route);
        }
    },
    route: {
        data() {
            if (this.$route.matched.length > 1) {
                // This is a nested view
                let idx = this.$route.matched.length - 2,
                    parent = this.$route.matched[idx];
                this.next_route = {
                    name: parent.handler.name,
                    params: parent.params
                };
            }
            let id = this.$route.params.discussion_id;
            API.discussions.get_discussion({id}, (response) => {
                this.discussion = response.obj;
            });
        }
    },
    methods: {
        confirm_delete() {
            this.deleting = true;
        },
        cancel_delete() {
            this.deleting = false;
        },
        delete() {
            API.discussions.delete_discussion({id: this.discussion.id},
                (response) => {
                    this.$refs.modal.close();
                }
            );
        },
        close_discussion() {
            this.send_comment(this.comment, true);
        },
        comment_discussion() {
            this.send_comment(this.comment);
        },
        send_comment(comment, close) {
            if (this.validate()) {
                API.discussions.comment_discussion({id: this.discussion.id, payload: {
                    comment: comment,
                    close: close || false
                }}, (response) => {
                    this.discussion = response.obj;
                    this.comment = null;
                });
            }
        }
    }
};
</script>
